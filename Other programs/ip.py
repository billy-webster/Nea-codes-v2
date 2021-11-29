#program will take the users ip and hostname and print the according latitude and longitude for the corresponding ip.

import requests #allows us to take/request data from web servers

import socket  #allows us to take user pc info





class ips:
    def __init__(self):
       self.hostname = socket.gethostname()    #defining the attributes of the class, establishing the variables for the pc name and ip adress 
       self.IPAddr = socket.gethostbyname(self.hostname)  
       self.Publicip = requests.get('https://api.ipify.org/').text

    
    def outputinfo(self):
        print("Your Computer Name is:" + self.hostname)    #first method which simply prints the attributes (ip and hostname)
        print("Your Computer Private IP Address is:" + self.IPAddr)
        print("Your Computer Public Ip Address is:" + self.Publicip)

    
    def outputlatlon(self):
        
        self.ip = self.Publicip   #creates new attribute as to stop any manipulation which will alter the output of other methods
        self.link1 = ("http://ip-api.com/json/{}").format(self.ip) #stores the link which is used to take the json data from
        self.request = requests.get(self.link1).json() #pulls the json data from the web link and tells python that it is a json format
        
        self.lat1=(self.request['lat']) #prints certain data from the json
        self.lon1=(self.request['lon'])
        print (self.lat1)
        print (self.lon1)

      
obj = ips() #defines the object
obj.outputinfo() #runs the method outputinfo
obj.outputlatlon() #displays the info of the lat and lon




#all processing done without organising the flow of the program
def maincode():
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    print("Your Computer Name is:" + hostname)    
    print("Your Computer IP Address is:" + IPAddr) 
    ip = ("92.17.161.222")
    link1 = ("http://ip-api.com/json/{}").format(ip)

    request = requests.get(link1).json()

    print(request['lat'],"lat")
    print(request['lon'],"lon")


lat= getattr(obj, 'lat1') #will globalise the attributes
lon= getattr(obj, 'lon1') #done so that the data can be acessed in seperate python files



#response = requests.get("http://ip-api.com/json/24.48.0.1").json()

#print(response['lat'])
#print(response['lon'])
#print(response['lat'])
#print(response['lon'])
