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

------------------------------SEANCE3 SUITE--------------------------------------------------------------------------

mon fichier farm.json
{
	"ferme_name": "premiere_ferme",
	"animal_list": [
		{
			"type": "vache",
			"age": "5anS",
            "sexe": "femelle",
            "birthday": "6/10/2020",
            "adult" :"4",
            "retirement": "2"
		},
    		{
      			"type": "mouton",
      			"age": "2ans",
                  "sexe": "femelle",
                  "birthday": "3/4/2020",
                  "adult" :"2",
                  "retirement": "6"
   		 },
   		 {
      			"type": "poule",
      			"age": "1an",
                  "sexe": "femelle",
                  "birthday": "12/08/2020",
                  "adult" :"3",
                  "retirement": "2"
    		}
	],


  	"ferme_name": "Deuxieme_ferme",
	"animal_list": [
    		{
			"type": "chien",
			"age": "8mois",
            "sexe": "male",
            "birthday": "9/11/2020",
            "adult" :"1",
            "retirement": "2"
		},
		{
			"type": "lapin",
			"age": "2mois",
            "sexe": "male",
            "birthday": "5/4/2020",
            "adult" :"4",
            "retirement": "2"
		}
	],

	"ferme_name": "Troisieme_ferme",
	"animal_list": [
		{
			"type": "chevre",
			"age": "2ans",
            "sexe": "femelLe",
            "birthday": "20/3/2020",
            "adult" :"2",
            "retirement": "5"
		}
	]
}

                     

---------------------mon fichier python :TP3.py------------------------------------------------------------

from TP3 import *
import datetime
import json




def farm_factory(farm_name, animal_description):

        my_current_farm = Farm(farm_name)

# for each animal in animal_description add it to the farm
        for my_current_farm in animal_description:
            my_current_farm = my_current_farm.__add_animal(type , age, sexe)
            return my_current_farm

if __name__ == "__main__":

	# Load JSON file into a variable
        with open('farm.json') as json_file:
            data = json.load(json_file)

	# Create farms list
        farm_list = []

	# For each farm in JSON file, create it and add it to the farm list

        for premiere_ferme in farm_list.append :
            farm_list.append(farm_factory('premiere_ferme', 'deuxieme_ferme', 'troisieme_ferme'))


	# The rest is the same as before.

	# We print the list of farms (and animals)
        for current_farm in farm_list:
            print(current_farm)


	# We start travelling to the future
            print("\nWe start the time...:\n")

        time_iteration = 0

        while time_iteration < 100:

		# Advance time of 28 days = 4 weeks
            future_farms_date = current_farms_date + datetime.timedelta(days = 28)

            print("\n\tAdvancing to : " + str(future_farms_date))

        time_iteration += 1

        for current_farm in farm_list:
            current_farm.pass_time(datetime.timedelta(weeks = 4))

            current_farms_date = future_farms_date

	# We print the list of farms (and animals)
        for current_farm in farm_list:
                print(current_farm)








