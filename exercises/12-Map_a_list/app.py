Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
    f_value = (x*9 / 5) + 32 
    return f_value

    
   
result = list(map(fahrenheit_values, Celsius_values))
print(result)
