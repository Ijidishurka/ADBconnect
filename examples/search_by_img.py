from ADBconnect import USB

phone = USB(device='67e345rf')  # indicate which device we will work with

button = phone.screen.search_image('img.png')  # search for coordinates on the screen where the photo is located

if button:
	phone.action.tap(button[0], button[1])  # tap
	print('tap')
else:
	print('button not found.')
	
	