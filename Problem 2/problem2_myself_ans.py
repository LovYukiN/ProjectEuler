Fib1,Fib2=1,2
smr=[Fib1,Fib2]
while (Fib1+Fib2<=4000000):
    tmp=Fib1+Fib2
    Fib1=Fib2
    Fib2=tmp
    smr.append(tmp)
print sum(value for value in smr if value%2==0)
