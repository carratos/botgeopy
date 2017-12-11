from scapy.all import *
#geolite2 is a library for getting a country name from and IP address
from geolite2 import geolite2
#Create or open file to store IP addresses to make a graph based on it.
file = open("botfile.txt", "w")
#time variable control window size
time = 0.0
count = 0.0
#dst and src stores how many packets are sent by the server and attacker respectively
dst = 0.0
src = 0.0
#Importing database for geolocation information
reader = geolite2.reader()
#geod is a dictionary containing country names and a counter for number of packets
geod = {}

#server is victim IP of botnet attack
server = "10.0.2.15"
#'bonesi.pcap' is the name of the file we wish to analyze
with PcapReader("bonesi.pcap") as pcap_reader:
        for pkt in pcap_reader:
                if pkt.haslayer(IP):
                        count = count + 1
                        if server in pkt[IP].dst:
                                dst = dst + 1
                                #Reads in current IP address as a string
                                data = reader.get(pkt[IP].src)
                                #print(pkt[IP].src)
                                if data != None:
                                        country = data['country']['names']['en']
                                        #print(country)
                                        if geod.get(country) == None:
                                                geod[country] = 0
                                        else:
                                                geod[country] = geod.get(country) + 1
                        else:
                                src = src + 1
                        if pkt.time - time > 5:
                                result = float(dst/count-src/count)
                                print(result)
                                file.write(str( result ) + "\n")
                                count = 0.0
                                dst = 0.0
                                src = 0.0
                                #Time is set to current value of pkt.time
                                time = pkt.time
print geod
file.close()
