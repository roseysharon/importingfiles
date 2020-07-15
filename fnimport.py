import fn #from fn import maximum,minimum
numbers=[1, 2, 3]
x=fn.maximum(numbers)
print(x)
y=fn.minimum(numbers)
print(y)

#other way of importing
from fn import maximum,minimum
numbers=[1, 2, 3]
x=maximum(numbers)
print(x)
y=minimum(numbers)
print(y)