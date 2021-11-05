theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def change_data(number):
    if number == 1:
        return 'wiki'
    else:
        return 'woko'


new_list = list(map(change_data,theBools))
print(new_list)
