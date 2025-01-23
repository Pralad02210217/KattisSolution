correctAnswer = 0
timeSum = 0
attempts = {}
A = True
while True:
    word = input()
    if word == '-1':  
        print(f'{correctAnswer} {timeSum}')
        break  
    time, ques, res = word.split(" ")
    if ques not in attempts:
        attempts[ques] = 0  
    if res == 'right':
        result = 20 * attempts[ques]
        correctAnswer += 1
        timeSum += int(time) + result
    attempts[ques] += 1
