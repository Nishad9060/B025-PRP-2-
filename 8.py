list = [3,2,6,4,8,5]
sum = 0
new = []
for i in range(len(list)):
    sum = sum + list[i]
    new.append(sum)
print(new)