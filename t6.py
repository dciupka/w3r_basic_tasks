'''5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Go to the editor
'''


fname = input('fname: ')
lname = input('lname: ')

print(f'{lname} {fname}')




'''
2.Something harder solution
name = 'Dawid Ciupka'
new_str=''
for i in name.split():
    i=i[::-1]
    new_str+=i+' '

print(new_str.rstrip())
'''