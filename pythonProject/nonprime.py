a = int(input("Enter strarting range : "))
b = int(input(("Enter ending range : ")))

def is_prime(num):
    if num < 2 : return True
    for i in range(2, (num//2)+1):
        if num/i == num//i:
            return True
    return False
for num in range(a, b+1):
        if is_prime(num):
            print(num)