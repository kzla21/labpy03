import random

def generate_random_numbers(n):
    random_numbers = []
    while len(random_numbers) < n:
        num = random.random()
        if num < 0.5:
            random_numbers.append(num)
    return random_numbers

# Meminta input nilai n dari pengguna
n = int(input("Masukkan jumlah bilangan acak yang diinginkan: "))
hasil = generate_random_numbers(n)
print("Bilangan acak yang lebih kecil dari 0.5:", hasil)
