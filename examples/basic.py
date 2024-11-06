import ADBconnect
import time

# ADBconnect.Phone(device='67e345rf')  # indicate which device we will work with

ADBconnect.screen()  # turn on your phone screen (or turn it off if it's already on)


print(ADBconnect.get_device_info())  # show information about the device


applications = ADBconnect.get_apps()  # get a list of all installed packages

for app in applications:
	print(app)

if 'org.telegram.messenger' in applications:  # if the telegram package is installed
	telegram = ADBconnect.run_app('org.telegram.messenger')  # launch telegram
	time.sleep(5)
	
	ADBconnect.screenshot('tg.png')  # create a screenshot called tg.png
	ADBconnect.swipe(360, 1440, 360, 730, 2000)  # swipe down with a delay of 2 seconds
	time.sleep(10)
	
	telegram.close()  # close telegram
	
ADBconnect.tap(200, 200)  # click on the screen at coordinates (x - 200, y - 200)

ADBconnect.reboot()  # Reboot the device
ADBconnect.power_off()  # Turn off the device

