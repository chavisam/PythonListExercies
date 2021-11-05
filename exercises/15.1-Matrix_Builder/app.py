#Import random
import random
random_number = random.randint(1,10)
the_list = []

#Create the function below:
def matrixBuilder(number):
    for i in range(number):
        the_list.append([1] * random_number)


matrixBuilder(random_number)

print(the_list)