#**********************Keyword arguments***************************
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))

fun(a=10, b=20,name= "john") # keyword is always passed as a string and not any other type
#fun(10="rahul",20="chetan")  # wrong way