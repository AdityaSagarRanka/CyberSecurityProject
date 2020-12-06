print("*****===***** OPTIONS *****===*****")

print("1. Vulnerability Scan")

print("2. System Health Scan")

print("3. Steganography")

print("4. Encryption")



a=input("\n Enter the option number you want to use : ")

if(a==1):

	print("\nWelcome to Vulnerability Scanning")

	execfile('cyber.py')

	

elif(a==2):

	print("\nWelcome to encryption")

	execfile('enc.py')

	

elif(a==3):

	print("\nWelcome to Steganography")

	execfile('steganography.py')



elif(a==4):

	print("\nWelcome to encryption")

	execfile('enc.py')

	

else:

	print("\nInvalid Option\n")
