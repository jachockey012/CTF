#!/usr/bin/python3

#---------------------------------------------------------------------#
# A script to en code a flag in morse code and then send for capture  #
# it encodes the paylod in the flags of the IP header                 #
# Might be funny to REF RFC 3514 and/or some Morse Code hero          #
#				With Love: Jake Coyne								  #
#---------------------------------------------------------------------#


from scapy.all import *

# Dictionary representing the morse code chart
morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}



def encode_flag(flag):
	flag = flag
	encoded_flag=''
	for i in flag:
		if i == ' ':
			print("You FOOL Read the Instructions.. <3 you")
		else:
			encoded_flag += morse[i]
			encoded_flag += ' '
	return(encoded_flag)

def gen_packets(src, dest, flag):
	ipPacket = IP()
	ipPacket.dst= dest
	ipPacket.src= src
	
	'''
	This loop will set the flags in the IP header based off moese code
	the flags look like this.
	4   2    1 
	E + DF + MF
	
	So for a char('J') we will see the morse ".---"
	This means 4 packets with the flags of 4,5,5,5
	or E, E+MF, E+MF, E+MF
	'''
	for i in flag:
		if i == '.':
			#4
			ipPacket.flag = 4
		if i == '-':
			#5
			ipPacket.flag = 5
		if i == ' ':
			#6
			ipPacket.flag = 6
		send(ipPacket/ICMP())



if __name__ == '__main__':
	'''
	Edit these values for the desired source and dest IP address
	if the the addresses are not valid a you will get dest unreachable

	For the flag I am assuming all CAPITAL with no space for simplicity
	it was the first morse dict I found on google
	'''
	sourceIP = '127.0.0.1'
	destIP = '127.0.0.1'
	flag = "YOURFLAG"
	flag_encoded = encode_flag(flag)
	gen_packets(sourceIP,destIP, flag_encoded)
	print("Done")