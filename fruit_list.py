fruit = ['apple', 'banana', 'grape', 'pear', 'orange']

print("the list of your favourite fruit is {}".format(fruit))

fruit.append('watermalten')
print(fruit)

fruit.remove('grape')
print(fruit)

fruit.insert(2, 'ab')
print(fruit)

remove_fruit = fruit.pop(3)
print(remove_fruit)
