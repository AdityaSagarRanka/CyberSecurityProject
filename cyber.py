print("*****===***** OPTIONS *****===*****")

print("1. XSS")

print ("2. SQLI")



a=int(input("\n Enter the option number you want to use : "))

if(a==1):

	print("\nWelcome to XSS")

	exec(open("./xss_scan http://www.hotelornate.com.pk").read())

	

elif(a==2):

	print("\nWelcome to SQLInjection")

	exec(open("./sqli_scan.py  http://www.hotelornate.com.pk").read())

	

else:

	print("\nInvalid Option\n")
