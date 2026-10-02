

import unittest
from unittest.mock import mock_open, patch

from lab4 import process_logs


class TestLogProcessor(unittest.TestCase):

    def test_process_logs(self):
        # Тестові дані (імітація реального логу)
        fake_log = (
            '213.109.238.193 - - [07/May/2017:00:08:35 +0300] "GET /question/edit.php HTTP/1.0" 303 440 "-" "Mozilla/5.0"\n'
            '195.182.22.209 - - [07/May/2017:00:16:22 +0300] "GET / HTTP/1.0" 200 23712 "-" "Mozilla/5.0"\n'
        )

        # Мокуємо зчитування файлу без реального файлу на диску
        with patch("builtins.open", mock_open(read_data=fake_log)):
            rx, tx = process_logs("fake.txt")

            # 33 B (перший запит) + 14 B (другий запит) = 47 B
            # 440 B + 23712 B = 24152 B
            self.assertEqual(rx, 47)
            self.assertEqual(tx, 24152)

    def test_process_logs_with_dash(self):
        # Перевірка випадку, коли замість байтів стоїть профіс '-'
        fake_log = '127.0.0.1 - - [07/May/2017:00:00:00 +0300] "POST /api HTTP/1.1" 500 - "-" "-"'

        with patch("builtins.open", mock_open(read_data=fake_log)):
            rx, tx = process_logs("fake.txt")

            self.assertEqual(rx, 19)
            self.assertEqual(tx, 0)


if __name__ == "__main__":
    unittest.main()
