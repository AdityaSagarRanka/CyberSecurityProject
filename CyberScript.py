import pyfiglet 
  
result = pyfiglet.figlet_format("The Cyber Sanjay", font = "banner3-D" ) 
print(result) 



print("*****===***** OPTIONS *****===*****")

print("1. Vulnerability Scan")

print("2. System Health Scan")

print("3. Steganography")

print("4. Encryption")





a=int(input("\n Enter the option number you want to use : "))

if(a==1):

	print("\nWelcome to Vulnerability Scanning")

	exec(open("./cyber.py").read())

	

elif(a==2):

	print("\nSystem Health info")

	exec(open("./syscheck.py").read())
	

elif(a==3):

	print("\nWelcome to Steganography")

	exec(open("./steganography.py").read())



elif(a==4):

	print("\nWelcome to encryption")

	exec(open("./encryption.py").read())


	

else:

	print("\nInvalid Option\n")
