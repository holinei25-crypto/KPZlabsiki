def reverse_words(text):
    """
    Розвертає всі букви кожного слова, залишаючи небуквені
    символи на своїх початкових позиціях.

    >>> reverse_words("abcd")
    'dcba'

    >>> reverse_words("abcd efgh")
    'dcba hgfe'

    >>> reverse_words("")
    ''

    >>> reverse_words("a1bcd efg!h")
    'd1cba hgf!e'

    >>> reverse_words(123)
    Traceback (most recent call last):
    ...
    TypeError: Аргумент повинен бути рядком
    """

    if not isinstance(text, str):
        raise TypeError("Аргумент повинен бути рядком")

    result = []

    for word in text.split(" "):
        letters = [char for char in word if char.isascii() and char.isalpha()]
        reversed_letters = letters[::-1]
        letter_index = 0
        new_word = []

        for char in word:
            if char.isascii() and char.isalpha():
                new_word.append(reversed_letters[letter_index])
                letter_index += 1
            else:
                new_word.append(char)

        result.append(''.join(new_word))

    return ' '.join(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    while True:
        text = input("Введіть текст: ")

        if text.isdigit():
            print("Помилка: введіть текст, а не тільки число.")
            continue

        try:
            print("Результат:", reverse_words(text))
            break
        except TypeError as error:
            print(error)

    input()
