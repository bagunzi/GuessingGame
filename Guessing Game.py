from random import randint
print('Im thinking in a value between 1 and 10. Can you guess it?')
pc=randint(1,10)
cont = 0
while True:
    n=int(input('Type a value: '))
    cont = cont + 1
    if n >= 11:
        cont = cont + 1
        print('Too high')
    if n == pc:
        break
print(f'Congratulations! I thought  {pc}. You won in the {cont} try! ')