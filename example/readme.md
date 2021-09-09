Running `solve.py` on `dotdash.pcapng` pcap will return:
`-.-. - ..-. -.--. -.. --- - -....- -.. .- ... .... -....- ..-. - .-- -.--.-`

If you put that in https://morsecode.world/international/translator.html

you will get: `CTF(DOT-DASH-FTW)` 

Keep in mind `{}` don't exist so we use `()`

*** To a defender it should be obvious what the covert channel is. However, they will not know what comination of `DF` and `EVIL` bits make up a `.` or `-` or ` `. So it is reccomended that there is a hint like name the file dotdash, talk about RFC 3514, and ensure they are aware of the flag format `CTF(ALL CAPS FLAG)` ***


You might even want to give them this dictonary to make it easier...

```
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
```
