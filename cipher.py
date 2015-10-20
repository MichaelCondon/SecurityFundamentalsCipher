#!/usr/bin/python
# Filename: cipher.py
from bitarray import bitarray #Import the BitArray Module (DO THIS ON ALL MACHINES)
import pickle
def main():
	print("Welcome to group 12's cipher")
	print("Please enter the path to the file you wish to Encrpyt")
	fileName = raw_input()

	plainText=open(fileName,'r') #Takes the path given via user input and assigns the file to object "PlainText", in read mode.
	
	#TODO: Remove as they are done
	#Implement Serialisation
	#Inverse method
	#P-BOX
	#S-BOX
	#Bit-Shift
	
	textBits = bitarray()
	textBits.frombytes(plainText.read(),16)
	print(textBits)
if __name__ == "__main__": main() #Defines the Main module as "Main" and not a library