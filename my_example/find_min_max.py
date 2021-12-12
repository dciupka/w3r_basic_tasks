lista = [1,2,3000,4,5,100,2000]
#---------------------------------------------
def maxValue(l):
    max_val=float('-inf')
    for v in l:
        if v>max_val:
            max_val=v
    return max_val

print(maxValue(lista))
#---------------------------------------------
#wbudowana funkcja Pythona
print(max(lista))
#---------------------------------------------
# Petla
'''Po pierwszej petli przypisuje max 1, ponieważ no jest więsze od -nieskończoności
w kolejnym obiegu petli przypisuj max =2
aż znajdzie najwieksza i juz jej nie zmieni no bo już znalazł
 '''
max = float('-inf')  #nieskończenie mała liczba
for v in lista:
    if v>max:
        max=v
print(max)
#---------------------------------------------
maxi =None
for val in lista:
    if maxi is None or val>maxi:
        maxi=val

print(maxi)
#---------------------------------------------
# z None
print("MIN VALUE:")
min = None
for v in lista:
    if min is None or v< min:
        min=v
print(min)


