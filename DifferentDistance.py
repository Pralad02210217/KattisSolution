while True:
    Numbers = list(map(float, input().split()))
    first = Numbers[0]
    p = Numbers[-1]

    if first == 0:
        break
    distance = (abs(Numbers[0] - Numbers[2])**p + abs(Numbers[1] - Numbers[3])**p)**(1/p)
    distance=round(distance,10)

    print(distance)
