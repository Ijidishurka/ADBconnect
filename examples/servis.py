import ADBconnect

ADBconnect.wifi(True)  # Turn on wifi

ADBconnect.set_proxy('123.156.789', 888)  # Enable proxy
ADBconnect.reset_proxy()  # Reset proxy

ADBconnect.bluetooth(False)  # Turn off bluetooth
ADBconnect.airplane_mode(True)  # Turn on airplane mode
ADBconnect.mobile_data(True)  # Enable mobile data

