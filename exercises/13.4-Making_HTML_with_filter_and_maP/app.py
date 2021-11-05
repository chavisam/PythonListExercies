all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors (obj):

	if obj['sexy']:
		return obj['label']

new_arr = list(filter(filter_colors,all_colors))

new_colors = list(map(lambda color: color['label'],new_arr))

def generate_li(color):
	return f'<li>{color}</li>'


result = list(map(generate_li,new_colors))

for i in result:
	print(i)