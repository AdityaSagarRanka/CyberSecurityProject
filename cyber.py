print("*****===***** OPTIONS *****===*****")

print("1. XSS")

print ("2. SQLI")



a=input("\n Enter the option number you want to use : ")

if(a==1):

	print("\nWelcome to XSS")

	execfile('xss_scan.py ')

	

elif(a==2):

	print("\nWelcome to SQLInjection")

	execfile('sqli_scan.py http://testphp.vulnweb.com/artists.php?artist=1')

	

else:

	print("\nInvalid Option\n")
