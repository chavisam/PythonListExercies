arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
newArr= []

for i in range(len(arr)-1,-1,-1):
    newArr.append(arr[i])

print(newArr)