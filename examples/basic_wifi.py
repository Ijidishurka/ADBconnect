from ADBconnect import WIFI
import time

phone = WIFI(ip='192.168.0.101')  # indicate which device we will work with

phone.action.screen()  # turn on your phone screen (or turn it off if it's already on)


print(phone.control.get_device_info())  # show information about the device


applications = phone.control.get_apps()  # get a list of all installed packages

for app in applications:
	print(app)

if 'org.telegram.messenger' in applications:  # if the telegram package is installed
	telegram = phone.control.run_app('org.telegram.messenger')  # launch telegram
	time.sleep(5)
	
	phone.screen.screenshot('tg.png')  # create a screenshot called tg.png
	phone.action.swipe(360, 1440, 360, 730, 2000)  # swipe down with a delay of 2 seconds
	time.sleep(10)
	
	telegram.close()  # close telegram
	
phone.action.tap(200, 200)  # click on the screen at coordinates (x - 200, y - 200)

phone.action.reboot()  # Reboot the device
phone.action.power_off()  # Turn off the device

