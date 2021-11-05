def lyrics_generator(arr):
    y = 0
    result = ''
    for i in arr:
        if i ==0:
            result = result + 'Boom '
            
        else:
            if y==2:
                result = result +'!!!Break the base!!! '
                y=0
            else:
                result = result +'Drop the base '
                y = y +1
    
    return result

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))

