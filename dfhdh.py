x = int(input("пиши число "))
if x < 0:
    for x in range(0,x -1, -1):
        print(x)
if x > 0:
    for x in range(x+1):
        print(x)
    