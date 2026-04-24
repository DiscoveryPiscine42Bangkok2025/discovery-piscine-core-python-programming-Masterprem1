a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
sum = a*b
print (f"{a} x {b} = {sum}")
if sum > 0 :
    print ("This result is positive.")
elif sum < 0 :
    print ("This result is negative.")
else :
    print ('This result is positive and negative.')