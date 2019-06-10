"""
def addNumbers(num1,num2):   # definition of addNumbers
    num3 = num1+num2
    #print(f"sum of {num1} and {num2} = {num3}")
    #return num3
    return none         #by default none is returned
result = addNumbers(23,-23)
print(result)
print(addNumbers(10,20)) # execution of addNumbers
addNumbers(100,200)
"""
#********************************************************************************************

def applyPromomCode(promocode, amount):
    if promocode is "FLAT50":
        return amount * 50//100
    elif promocode is "FLAT30":
        return amount * 30//100
    else:
        return amount * 10//100

total = 1000
"""
#discount = applyPromomCode("FLAT50", total)
#total = total -discount
print("Please pay: \u20b9", total - applyPromomCode("Flat50", total))     #expert use
"""

#************************************************************************************************8

fun = applyPromocode
print("Fun is: ",fun)
print("Please pay: \u20b9", total - fun("Flat50", total))     #expert use

# create a function which applies promocode on the basis of these conditions
#1. flat50 can work on if total is greater than 1000
#2. flat 30 if total is grater tha 500 but less than 1000
#3. we can propose use to apply a promocode which is more beneficial for him/her
#4. make sure of various testcases