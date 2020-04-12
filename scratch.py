num=int(input("enter the number of shops:"))
print("slot1: 8am to 12pm")
print("slot2: 12pm to 4pm")
print("slot3: 4pm to 8pm")

a1=[]
a2=[]
a3=[]
for j in range(1,num+1,3):
    a1.append(j)
for j in range(2,num+1,3):
    a2.append(j)
for j in range(3,num+1,3):
    a3.append(j)
a4=[]
a5=[]
a6=[]
a7=[]
a9=[]
a8=[]
a4,a5,a6,a7,a8,a9=a1,a2,a3,a1,a2,a3
k=[a1,a2,a3,a4,a5,a6,a7,a8,a9]


for j in range(1,7,1):
    h=0
    print('day',j,':')
    for i in range(1,4,1):
        print('slot',i,':',end='')
        print(k[j+h-1])
        h=h+1
    print('')