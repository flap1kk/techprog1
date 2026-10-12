print('Hello world!')
try:
    n, m = map(int, input('Enter two nums: ').split())
except ValueError:
    print("Возможно, вы ввели не числа..")
    exit()

print(f"{n} + {m} = {n+m}")