print("Hello Good morning!")
print("I'm  Here to learn  while Loop")
i = 1
while i <= 10:
    print(i)
    i += 1
print("------------------continue-----------------------------")
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue

    print(i)
    i += 1

print("------------------break-----------------------------")

i = 1
while i <= 20:
    if i == 5:
        break
    print(i)
    i +=1
#Adding For loop:
for i in range(5):
    a=int(input("enter A :"))
    b = int(input("enter B :"))
    print(a+b)