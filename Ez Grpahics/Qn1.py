#Calculating possible  smallest combination of coins

input = int(input("Enter number of Cents: "))
varQuaters = input//25
varDimes = (input-(varQuaters * 25))//10
varNickle = (input-((varDimes*10)+(varQuaters*25)))//5
varPenny = input - ((varQuaters*25)+ (varDimes*10) + (varNickle*5))
print ("")
print("The possible  smallest combination of coins are:")
print("Pennies: {}".format(varPenny))
print("Nickles: {}".format(varNickle))
print("Dimes: {}".format(varDimes))
print("Quarters: {}".format(varQuaters))
