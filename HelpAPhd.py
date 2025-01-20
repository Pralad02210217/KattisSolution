n= int(input())

for i in range(n):
    text = input()
    if text == 'P=NP':
        print('skipped')
    else:
        num1, num2 = map(int, text.split('+'))
        print(num1+ num2)
