print ("Enter a number less than 25")
a = int(input())
if a > 25 :
    print ("Error")
else :
    for i in range(26-a):
        print (f"Inside the loop, my variable is {a}")
        a += 1
