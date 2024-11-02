# Program menghitung total keuntungan investasi selama 8 bulan
def calculate_profit():
    initial_capital = 100_000_000  # Modal awal 100 juta
    profit_percentage = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]  # Persentase laba setiap bulan
    total_profit = 0  # Variabel untuk menyimpan total keuntungan

    for month, percentage in enumerate(profit_percentage, start=1):
        monthly_profit = initial_capital * percentage  # Keuntungan bulan ini
        total_profit += monthly_profit  # Tambahkan keuntungan bulan ini ke total keuntungan
        print(f"Bulan {month}: Laba {percentage * 100}% = Rp {int(monthly_profit)}")

    print("\nTotal keuntungan selama 8 bulan adalah: Rp", int(total_profit))

# Menjalankan fungsi untuk menghitung keuntungan
calculate_profit()
