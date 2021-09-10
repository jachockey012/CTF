# CTF
Anything CTF Stuff. 

The script (`gen.py`) can be used to create a flag. You need to change some Vars in main and make sure the flag is all caps and no spaces. 

## The way it works. 
	BLUF: The IP header flags DF and Evil are maniupliated based off Morse code `'.'` or `'-'`.
	

	We set the flags in the IP header based off moese code
	the flags look like this.
	4   2  6
	E + DF Space
	
	So for a char('J') we will see the morse ".---"
	This means 4 packets with the flags of 2,4,4,4
	or E, E+MF, E+MF, E+MF

	SOS = ... --- ...
	OR 22264446222
	That means the packets would be in order of:
	DF DF DF EDF E E E EDF DF DF DF
	1  2  3  4   5 6 7 8   9  10 11 
