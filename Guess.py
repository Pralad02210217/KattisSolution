lowerLimit = 1
upperLimit = 1000

while True:
    guess = (lowerLimit+ upperLimit)//2
    print(guess)
    resp = input()
    if resp == 'lower':
        upperLimit = guess
    elif resp == 'correct':
        break
    else:
        lowerLimit = guess+1