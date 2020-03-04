 SENDING
 -------------------------------------------------------------
 import socket
   
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = "Hello, World!"
    
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE
   
   sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
  1 sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
  ---------------------------------------------------------------
  RECIEVING
  ----------------------------------------------------------------
   import socket
    
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    
   while True:
       data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
       print "received message:", data
