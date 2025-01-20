import math

n = int(input())
g=9.81

for i in range(n):
    v0,theta,x1,h1,h2 = map(float, input().split(' '))
    
    theta = theta * (math.pi/180)
    t = x1/ (v0* math.cos(theta))
    y = (v0*t*math.sin(theta)) - 1/2*(g* t* t)
    
    if h1+1 < y <h2-1 :
        print('Safe')
    else:
        print('Not Safe')
    