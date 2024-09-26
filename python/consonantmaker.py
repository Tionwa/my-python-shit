import re
import hashlib
import wave

with open("input.txt") as input:
    script = input.read()

## Converting to hash
#hashstr = hashlib.sha256(script.encode())
#print(hashstr.hexdigest())

## Consonants / Vowels only

#consonant = re.sub(r'[^bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ \s*]', '', script)
#with open ("output script.txt", "w") as output:
#    output.write(consonant)

## 2nd letter only

#secondletter = script[::2]

#with open ("output script.txt", "w") as output:
#    output.write(secondletter)

## Convert to hex

hexdata = script.encode().hex().upper()
filtereddata = hexdata # (eg 00010A)
#filtereddata = re.sub(r'(.{2})', r'0x\1 ', hexdata) (eg 0x00 0x01 0x0A)

print(filtereddata)
with open("hexscript.txt", "w") as convert:
    convert.write(filtereddata)
    