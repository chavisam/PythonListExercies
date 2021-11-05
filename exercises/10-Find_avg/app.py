my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:

data = 0

def average(list):
    list_length= len(list)

    sumNumber=0

    for i in list:
        sumNumber = sumNumber + i 
    
    result = sumNumber/list_length

    return result

print(average(my_list))