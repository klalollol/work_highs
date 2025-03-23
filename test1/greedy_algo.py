coins=[1,2,5,10,20,50,100,500,1000]
money=int(input("input the number: "))
x=len(coins)
while money>0:
    x=x-1
    while money>=coins[x]:
        print(coins[x])
        money=money-coins[x]
print(x)
