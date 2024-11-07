from ADBconnect import USB

phone = USB(device='67e345rf', adb_path=r";C:\Users\ijidishurka\platform-tools")  # indicate the path to adb


phone.action.tap(350, 600)  # tap the screen

phone.action.input_text('hello Ijidishurka!')  # enter text in the input field
phone.action.send_notification('hello :>')  # display a notification

phone.action.set_brightness(50)  # set brightness level
phone.action.set_volume(15)  # change volume
