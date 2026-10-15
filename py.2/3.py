n = int(input())

for i in range(1, n + 1):
    t = i
    d = True
    
    while t > 0:
        c = t % 10
        
        if c != 0 and i % c != 0:
            d = False
            break
            
        t = t // 10
        
    if d:
        print(i, end=" ")
