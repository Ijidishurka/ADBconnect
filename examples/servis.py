from ADBconnect import USB

phone = USB(device='67e345rf')  # indicate which device we will work with

phone.servis.wifi(True)  # Turn on wifi

phone.servis.set_proxy('123.156.789', 888)  # Enable proxy
phone.servis.reset_proxy()  # Reset proxy

phone.servis.bluetooth(False)  # Turn off bluetooth
phone.servis.airplane_mode(True)  # Turn on airplane mode
phone.servis.mobile_data(True)  # Enable mobile data

