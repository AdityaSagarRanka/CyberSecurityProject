print("*****===***** OPTIONS *****===*****")

print("1. Encrypt")

print ("2. Hash")

print ("3. Back")


a=int(input("\n Enter the option number you want to use : "))

if(a==1):

	print("\nEncrypt your text her, you muggle")

	exec(open("./encrypt.py").read())

	

elif(a==2):

	print("\nHash it out, here!")

	exec(open("./hash.py").read())
	
elif(a==3):

	exec(open("./CyberScript.py").read())

	

else:

	print("\nInvalid Option\n")

print("1. Back")
print("2. Exit")

b = int(input("Choose an option: "))

if(b==1):
	exec(open("./encryption.py").read())
elif(b==2):
    exit()
else:
    print("Invalid input")