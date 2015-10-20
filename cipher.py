#!/usr/bin/python
# Filename: cipher.py
from bitarray import bitarray #Import the BitArray Module (DO THIS ON ALL MACHINES)
import pickle

#Returns the inversed bits
def inverse(bits):
	bitlist = list(bits)
	for i in range (0,16):
		bit = bitlist[i]
		if bit == "0":
			bit = "1"
		else:
			bit = "0"
		bitlist[i] = bit
	inversedbits = ''.join(bitlist)
	return inversedbits

#Slices the text into smaller portions (in order to be 16bits)
def tolist(text):
	i = 0
	textlist = []
	while (i < len(text)):
		seq = ""
		if (i+2) > len(text):
			seq = (text[i]," ")
		else:
			seq = (text[i],text[i+1])
		var =  ''.join(seq)
		textlist.append(var)
		i = i+2
	return textlist


def main():
	print("Welcome to group 12's cipher")
	#print("Please enter the path to the file you wish to Encrpyt")
	#fileName = raw_input()

	plainText=open("plain.txt",'r') #Takes the path given via user input and assigns the file to object "PlainText", in read mode.
        text = plainText.read()
        #print(text)

	#TODO: Remove as they are done
	#Implement Serialisation
	#P-BOX
	#S-BOX
	#Bit-Shift


	textlist = tolist(text)

	#Code for testing purposes
	for block in textlist:
		textBits = bitarray()
		textBits.frombytes(block)
		print("before: "+textBits.to01())
		inversedbits = inverse(textBits.to01())
		print("after : "+inversedbits)




if __name__ == "__main__": main() #Defines the Main module as "Main" and not a library
