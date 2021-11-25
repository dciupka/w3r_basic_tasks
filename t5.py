'''Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''

# solution 1
sample_data = "3, 5, 7, 23"
lista = sample_data.split(',')
print('List: ', lista)
print('Tuple: ', tuple(lista))


'''
# solution 2
# not fully correct

sample_data = "3, 5, 7, 23"
empty_list=[]
for i in sample_data:
    try:
        num=int(i)
        x=str(num)
        empty_list.append(x)
    except ValueError:
        pass

print(f'List: {empty_list}')
print(f'Tuple: {tuple(empty_list)}')
'''

