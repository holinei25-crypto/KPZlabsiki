import re


def get_log_lines(file_name):
    """Читаємо файл по одному рядку через генератор (щоб зберегти пам'ять)."""
    with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            yield line


def process_logs(file_name):
    """Рахуємо сумарну кількість прийнятих та надісланих байтів."""
    total_received = 0
    total_sent = 0

    for line in get_log_lines(file_name):
        # Витягуємо рядок запиту в лапках та байти відповіді після коду 200/303/тощо
        match = re.search(r'"(.*?)" \d{3} (\d+|-)', line)
        if match:
            request_str = match.group(1)
            sent_str = match.group(2)

            # Прийняті байти — це довжина самого HTTP-запиту
            received_bytes = len(request_str.encode("utf-8"))

            # Надіслані байти — розмір відповіді від сервера (якщо '-', то 0)
            sent_bytes = int(sent_str) if sent_str != "-" else 0

            total_received += received_bytes
            total_sent += sent_bytes

    return total_received, total_sent


if __name__ == "__main__":
    file_name = "2017_05_07_nginx.txt"

    try:
        rx, tx = process_logs(file_name)

        print("=== ЗВІТ ПО ТРАФІКУ З ВЕБ-СЕРВЕРА ===")
        print(f"Прийнято (від клієнтів): {rx:,} B")
        print(f"Надіслано (від сервера):  {tx:,} B")
        print(f"Загальний трафік:         {rx + tx:,} B")

    except FileNotFoundError:
        print(f"Помилка: Файл '{file_name}' не знайдено в папці з кодом!")
