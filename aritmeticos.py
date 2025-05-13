#Valores aritmeticos
n1 = int(input('Say a number: '))
n2 = int(input('Say a other number:'))

if n1 > n2:
    print(f'The number {n1} is bigger than {n2}.' )
elif n1 < n2:
    print(f'The number {n1} is smaller than {n2}.')
else:
    print('The numbers are the same')

print(f'The summ {n1} + {n2} is {n1+n2}.')