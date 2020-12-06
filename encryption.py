print("*****===***** OPTIONS *****===*****")

print("1. Encrypt")

print ("2. Hash")



a=int(input("\n Enter the option number you want to use : "))

if(a==1):

	print("\nEncrypt your text her, you muggle")

	exec(open("./encrypt.py").read())

	

elif(a==2):

	print("\nHash it out, here!")

	exec(open("./hash.py").read())

	

else:

	print("\nInvalid Option\n")
