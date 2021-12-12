import random
empty_dic = dict()
print(empty_dic)

empty_dic['key']='value'
empty_dic['cos']=1
empty_dic['names']=['dawod','mariola','mikolaj','rena']
print(empty_dic)

tablica_pomiarowa=dict()
for pomiar in range(10):
    tablica_pomiarowa[f'pomiar {pomiar}']=random.random()
print(tablica_pomiarowa)
print(tablica_pomiarowa['pomiar 2'])
print(len(tablica_pomiarowa))