people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:


def deletePerson(person_name):
    newPeople =[]
    #Your code go here:
    for i in people:
        if i!=person_name:
            newPeople.append(i)
    return newPeople    


print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))