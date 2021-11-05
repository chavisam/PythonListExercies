chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    newList = []
    for i in list1:
        newList.append(i)
    
    for i in list2:
        newList.append(i)
    
    return newList
    
print(merge_list(chunk_one, chunk_two))
