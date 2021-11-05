
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filter_function(name):
    if name.startswith('R'):
        return name

resulting_names = list(filter(filter_function,all_names))
print(resulting_names)




