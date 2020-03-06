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
      
      -----------------------------------------------------------------------------------------------------------------------------
      ------------------------SEANCE2-----------------------------------------
      
      
      Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Animals :
	def __init__(self,regime,quantite,nb):
		self.regime = regime
		self.quantite = quantite
		self.nb = nb

		
>>> class mammiferes(Animals) :
	def __init__(self,regime,quantite,nbredepatte):
		self.regime = regime
		self.quantite = quantite
		self.nbredepatte = nbredepatte
		def __init__(self)
		
SyntaxError: invalid syntax
>>>  class mammiferes(Animals) :
	def __init__(self,regime,quantite,nbredepatte):
		self.regime = regime
		self.quantite = quantite
		self.nbredepatte = nbredepatte
		def __init__(self):
			
SyntaxError: unexpected indent
>>> class mammiferes(Animals) :
	def __init__(self,regime,quantite,nbredepatte):
		self.regime = regime
		self.quantite = quantite
		self.nbredepatte = nbredepatte
		def __init__(self):
		    return self.regime, self.quantite,self.nbredepatte

		
>>> class animal_marins(Animals) :
	def __init__(self,regime,quantite):
		self.regime = regime
		self.quantite = quantite
		def __init__(self):
		    return self.regime, self.quantite

		
>>> class domestiques(mammiferes) :
	def __init__(self,regime,quantite,nbredepatte,nb):
		self.regime = regime
		self.quantite = quantite
		self.nbredepatte = nbredepatte
		self.nb = nb
		def __init__(self):
		    return self.regime, self.quantite,self.nbredepatte,self.nbr

		
>>> class nondomestiques(mammiferes) :
	def __init__(self,regime,quantite,nbredepatte,nb):
		self.regime = regime
		self.quantite = quantite
		self.nbredepatte = nbredepatte
		self.nb = nb
		def __init__(self):
		    return self.regime, self.quantite,self.nbredepatte,self.nbr

		
>>> if __name__ == "__main__":
	mammiferes = mammiferes("lapin")
    print(mammiferes)
 



    mammiferes = {}
    mammiferes["lapin"]=mammifere
    
SyntaxError: unindent does not match any outer indentation level
>>> 
 RESTART: C:/Users/Mbathie Aminata/AppData/Local/Programs/Python/Python37/e.py 
>>> 

