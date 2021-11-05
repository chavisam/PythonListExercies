incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]
transformedData = ''
#Your code go here:
def my_var (data):
	transformedData = data['name'] +' '+ data['lastName']
	return transformedData


new_list = list(map(my_var,incomingAJAXData))
print(new_list)

