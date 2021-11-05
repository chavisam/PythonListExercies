par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:

for i in par:
    i=i.lower()
    if i == ' ':
        ''
    else:
        if counts.__contains__(i):
            counts[i]=counts[i]+1
        else:
            counts[i]=1
    

print(counts)
