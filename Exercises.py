def pattren(n):
    for i in range(n):
        for j in range(n, i, -1):
           print(' ', end="")
        print("*", end="")
        if i!=0:
            for j in range(2*i-1):
                print(" ", end="")
            print("*", end="")
           
        print()
    for i in range(i+1):
        for j in range():
            print(" ",end="")
            
            
        print()
    
pattren(4)