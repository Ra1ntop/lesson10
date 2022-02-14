
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")


print("k! = 1 * 2 * 3 * ... * k")
k = int(input("Введите k: "))
Mul = 1
for i in range(k):
    Mul *= i
print(Mul , "$")
