import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

print'-'*80
print"A tool Created by Antonio C."
print'-'*80

#Ask for input
remoteServer =  raw_input("Enter a remote host to scan on the network: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice Banner with informatioon in which host we are about to scan
print"-"*60
print"[+] Please wait, scanning remote host on yout network...",remoteServerIP
print"-"*60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it scans through all ports  1 and 1024)
# We also put in some error handling for errors

try:
	for port in range(1,1025):
	    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    result = sock.connect_ex((remoteServerIP, port))
	    if result == 0:
	       print"[+] Port {}: Open".format(port)
	    sock.close()

except KeyboardInterrupt:
	print "[+] You Pressed Ctrl+C"
	sys.exit()

except socket.gaierror:
	print "[+] Hostname could not be resolved. Exiting program"
	sys.exit

#checking the time again
t2 = datetime.now()

# Calculates the difference of timeto see how long it took the script
total = t2 - t1
#printing the info to screen
print"[+] Scanning Completed in: ",total

