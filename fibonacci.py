inpStr = input("Give number")
inp=int(inpStr)
print (inp)
fib = []
pre1 = 0
pre2 = 1
cur = 1
if inp <= 0:
    print ("error")
if inp == 1:
    print("[0]")
elif inp == 2:
    print ("[0,1]")
else:
    fib.append(0)
    fib.append(1)
    for d in range( inp-2):
        cur = pre1 + pre2
        pre1 = pre2
        pre2 = cur
        
        fib.append(cur)
        
print (fib)
