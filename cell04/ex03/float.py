a = (input("Enter a number: "))
number = a.replace('.','',1).isdigit()
if number :
    num = float(a)

    if num.is_integer() :
        print ("This number is an integer.")
    else :
        print ("This number is a decimal.")
