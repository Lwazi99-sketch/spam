#Write a program to generate a personalised spam message based on the user's full name, country and a sum of money
#Lwazi Somtsewu
#31 April 2024

name=str(input("Enter first name:\n"))
surname=str(input("Enter last name:\n"))
money =int(input("Enter sum of money in USD:\n"))
country= str(input("Enter country name:\n"))
me= (30/100)* money
print("")
print("Dearest" ,name, end="\n")
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk",surname,end= ", your long lost relative from Mapsfostol.\n")
print("My father left the sum of", money,end="USD for us, your distant cousins.\n")
print("Unfortunately, we cannot access the money as it is in a bank in",country, end=".\n")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount -",me ,end = "USD,\n")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",surname)
