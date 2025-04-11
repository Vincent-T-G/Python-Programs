#Program written in the learning of while else construct
#Probelem statement: Consider a list of fruits the includes 4 types of fruits:
#apple, banana, mango and strawberry. Write a program to determine whether the fruit orange is present in the list

fruits = ['apple', 'banana', 'mango', 'strawberry']
fruits_len = len(fruits)
index = 0

while index < fruits_len:
    if fruits[index] == 'orange':
        print('Orange is available,')
        break
    index += 1
else:
    print('Orange is not available.')