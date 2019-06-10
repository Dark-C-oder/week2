def addNumbers(num1,num2,num3=0):   # to make the function dynamic
     # def addNumbers(num1,num2=0,num3):   # cannot do this # sequence will be right tto left
    sum = num1+num2+num3
    print("sum is = ", sum)
print("addnumbers is: ", addNumbers())
#addNumbers(10,20)
#addNumbers(10,20,30)


def addNumbers(num1, num2, num3, num4):  # to make the function dynamic
    sum = num1 + num2 + num3+num4
    print("sum is = ", sum)
    print("addnumbers is: ", addNumbers())
addNumbers(10,20)
addNumbers(10,20,30)