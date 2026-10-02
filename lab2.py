from decimal import Decimal, ROUND_HALF_UP

def get_decimal(prompt):
    while True:
        raw = input(prompt).replace(",", ".").strip()
        try:
            val = Decimal(raw)
            if val > 0:
                return val
            print("❌ Число має бути більше 0!")
        except Exception:
            print("❌ Некоректний ввід! Введіть число.")

print("=== ДЕПОЗИТНИЙ КАЛЬКУЛЯТОР ===")
amount = get_decimal("Введіть початкову суму (грн): ")
rate = get_decimal("Введіть річну ставку (%): ")

years_input = input("Введіть термін у роках [Натисніть Enter для 2 років]: ").strip()
years = int(years_input) if years_input.isdigit() and int(years_input) > 0 else 2
months = years * 12

monthly_rate = rate / Decimal("100") / Decimal("12")
balance = amount

print(f"\n{'Місяць':^8} | {'Нараховано %':^15} | {'Баланс':^15}")
print("-" * 44)

for m in range(1, months + 1):
    interest = (balance * monthly_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    balance += interest
    print(f"{m:^8} | {interest:>11.2f} грн | {balance:>11.2f} грн")

print("=" * 44)
print(f"Початкова сума:  {amount:.2f} грн")
print(f"Прибуток:        {balance - amount:.2f} грн")
print(f"Кінцева сума:    {balance:.2f} грн")

input("\nНатисніть Enter для виходу...")
