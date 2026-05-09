list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(item) for item in list_of_strings]
result = [ evennum for evennum in numbers if evennum % 2 == 0 ]
print(result)