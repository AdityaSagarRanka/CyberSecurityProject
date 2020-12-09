print("*****===***** OPTIONS *****===*****")

print("1. XSS")

print ("2. SQLI")

print ("3. Recon")

print ("4. Back")



a=int(input("\n Enter the option number you want to use : "))

if(a==1):

	print("\nWelcome to XSS")

	exec(open("./xss_scan").read())	

elif(a==2):

	print("\nWelcome to SQLInjection")

	exec(open("./sqli_scan.py").read())

elif(a==3):
	print("\nWelcome to Recon")
	
	exec(open("./runsh.py").read())
	
elif(a==4):

	exec(open("./CyberScript.py").read())
	

else:

	print("\nInvalid Option\n")

print("1. Back")
print("2. Exit")

b = int(input("Choose an option: "))

if(b==1):
	exec(open("./CyberScript.py").read())
elif(b==2):
    exit()
else:
    print("Invalid input")