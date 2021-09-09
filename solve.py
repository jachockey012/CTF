#!/usr/bin/python3

#---------------------------------------------------------------------#
# A script to en code a flag in morse code and then send for capture  #
# it encodes the paylod in the flags of the IP header                 #
# Might be funny to REF RFC 3514 and/or some Morse Code hero          #
#				With Love: Jake Coyne								  #
#---------------------------------------------------------------------#


from scapy.all import *
import time

packets = rdpcap('sos_icmp.pcapng')
flag1 = ''

# Because we know there are only 3 possible combinitations of 
# flags lets loop through them all decode and see what is right

for packet in packets:
	if packet.haslayer(ICMP) and packet.payload.type == 8:
		if packet.flags == 'DF':
			flag1 += '.'
		if packet.flags == 'DF+evil':
			flag1 += ' '
		if packet.flags == 'evil':
			flag1 += '-'
print(flag)

'''

