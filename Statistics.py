i = 1

try:
    while True:
        currentNumber = list(map(int, input().split()))

        n = currentNumber[0] 
        data = currentNumber[1:]  

        NumberMax = max(data)
        NumberMin = min(data)
        NumberRange = NumberMax - NumberMin

        print(f"Case {i}: {NumberMin} {NumberMax} {NumberRange}")
        i += 1

except EOFError:
    pass  
