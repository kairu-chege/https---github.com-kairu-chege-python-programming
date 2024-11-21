a = 5
b = 9
k = int(input('Enter a number')) #assign the input value to k
g = b/k #divide the initial set values by the input value

try:
    print(b/a)
    
except ZeroDivisionError as e:
    print('You cannot divide a number by zero', e)
except ValueError as e:
    print('You cannot divide a number by zero', e)
except Exception as e:
    print('You cannot divide a number by zero', e)
finally:
    print('Muy bien', g)