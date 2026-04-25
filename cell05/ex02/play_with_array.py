list = [2, 8, 9, 48, 8, 22, -12, 2]
print (list)
for i in range(len(list)) :
    list[i] += 2
a_list = [x for x in list if x > 5]
print (a_list)