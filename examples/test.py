import ADBconnect

easyADB.Phone(adb_path=r";C:\Users\ijidishurka\platform-tools")  # indicate the path to adb


easyADB.tap(350, 600)  # tap the screen

easyADB.input_text('hello Ijidishurka!')  # enter text in the input field
easyADB.send_notification('hello :>')  # display a notification

easyADB.set_brightness(50)  # set brightness level
easyADB.set_volume(15)  # change volume
