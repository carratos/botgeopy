# botgeopy
This program takes in a pcap file and outputs to terminal a number between -1 and 1 depended on the ration a traffic to and from a websever respectively. This program was designed in order to analyze a pcap that was created using the program BoNeSi which is used to create custom packets to send to a server, in this case, used in a botnet simulation usingn the 50k-bots option. The program makes use of scapy for IP analysis as well as geolite2 to determine approximate country location of an IP address and place that in a dictionary to later determine the country of origin of simulated attack.

This program was developed in a linux environment and may no work on all systems.
