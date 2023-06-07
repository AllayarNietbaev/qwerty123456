import random
a = random.randint(1,10)
chances = 7
b = int(input('num='))
start = 0
stop = 7
while start<=stop:
    if b<a:
        print('ulkenrek san jaz')
    elif a>b:
        print('kishirek san jaz')
    else:
        print('ten')
        break
    b = int(input('num=')) 
    print(a)
    start+=1