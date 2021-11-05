#Remember import random function here:
import random;


my_list = [4,5,734,43,45]

#The magic is here:

def insert_ten():
    for i in range(10):
        random_number = random.randint(0,100)
        my_list.append(random_number)

insert_ten()
print(my_list)