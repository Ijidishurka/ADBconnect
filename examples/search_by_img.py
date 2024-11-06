import ADBconnect

button = ADBconnect.search_image('img.png')  # search for coordinates on the screen where the photo is located

if button:
	ADBconnect.tap(button[0], button[1])  # tap
	print('tap')
else:
	print('button not found.')
	
	