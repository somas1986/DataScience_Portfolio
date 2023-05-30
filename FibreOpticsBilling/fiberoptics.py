#Fiber Optics Billing - Project
#Author Soma Shekar Vayuvegula
#03/31/2022

#Change#:2
#Change(s) Made: Added code to issue receipt to user for fiber optics installation with applicable discounts
#Date of Change: 03/31/2022
#Author: Soma Shekar Vayuvegula
#Change Approved by: Michael Eller
#Date Moved to Production: 03/31/2022

print('\t\tSoma Fiber Optics Corp\n')
print('Welcome user! \n')

#companyName holds company name of the user
companyName = input('Enter your Company name: \t')

#fiberOpticLength holds number of feet of fiber optic cable to be installed
fiberOpticLength = input('Enter number of feet of fiber optic cable to be installed: \t')


#pricePerFoot is a constant with applicable discounts
if int(fiberOpticLength) > 500:
    pricePerFoot = 0.50
elif int(fiberOpticLength) > 250:
    pricePerFoot = 0.70
elif int(fiberOpticLength) > 100:
    pricePerFoot = 0.80
else:
    pricePerFoot = 0.87

#totalCost is obtained by multiplying pricePerFoot and fiberOpticLength
totalCost = float(fiberOpticLength) * pricePerFoot

# Print invoice with Company name, length of fiber optics to be installed, price per foot of fiber optics installation and Total installation cost
print('\n\n\n\t\tSoma Fiber Optics Corp')
print('\t\t\t\tINVOICE')
print('=============================================')

print('Company Name: \t' + companyName)
print('Length of fiber optic cable to be installed: \t' + fiberOpticLength)
print('Price per foot of Fiber optics installation: \t $ ' + "{:.2f}".format(pricePerFoot))

print('Total Installation Cost: \t $ ' + "{:.2f}".format(totalCost))

