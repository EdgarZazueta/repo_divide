num = int(input("Da un entero: "))

if num%15==0:
    print("Divisible entre 3 y 5")
else num%3==0:
    print("No es divisible entre 3")
if num%5 == 0:
    print("Divisible entre 5")
else:
    print(num)

print(Good bye)
