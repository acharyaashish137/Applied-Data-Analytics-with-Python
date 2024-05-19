# Calculating Income Tax

inputAmount=0
tax=0
inputAmount=int(input("Enter Income:"))
if inputAmount<=50000:
    tax=inputAmount*0.001
elif inputAmount>50000 and inputAmount<=75000:
    tax=inputAmount*0.002
elif inputAmount>75000 and inputAmount<=100000:
    tax=inputAmount*0.003
elif inputAmount>100000 and inputAmount<=250000:
    tax=inputAmount*0.004
elif inputAmount>250000 and inputAmount<=500000:
    tax=inputAmount*0.005
else:
    tax=inputAmount*0.06
print ("")
print("Income tax:${0}".format(tax))
