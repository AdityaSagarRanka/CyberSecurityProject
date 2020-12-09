print("*****===***** OPTIONS *****===*****")

print("1. XSS")

print ("2. SQLI")

print ("3. Recon")



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
	

else:

	print("\nInvalid Option\n")
