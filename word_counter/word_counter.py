with open('book.txt','r') as f:
    file = f.readlines()
    print(file)
    word_dic = {}
    for element in file:
        lines = element.split()
        for word in lines:
            count = lines.count(word)
            if word not in word_dic:
                word_dic={word:count}


lista = [1,2,3000,4,5,100,2000]

def maxValue(l):
    max_val=float('-inf')
    for v in l:
        if v>max_val:
            max_val=v
    return max_val

print(maxValue(lista))
print(max(lista))


max = float('-inf')
for v in lista:
    if v>max:
        max=v
print(max)

max_num= float('-inf')
print(max_num)
print(type(max_num))