def find_largest_number():
    largest_number = None

    while True:
        try:
            num = float(input("Masukkan bilangan (masukkan 0 untuk berhenti): "))
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

        if num == 0:
            break

        if largest_number is None or num > largest_number:
            largest_number = num

    return largest_number

# Menjalankan fungsi
largest = find_largest_number()
print("Bilangan terbesar yang diinput adalah:", largest)
