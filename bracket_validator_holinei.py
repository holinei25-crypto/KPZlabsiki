def validate_brackets(text: str) -> bool:
    """
    Перевіряє баланс дужок (), {}, <> у рядку.
    Повертає True, якщо рядок валідний, або піднімає ValueError із зазначенням позицій помилок.
    """
    bracket_map = {')': '(', '}': '{', '>': '<'}
    open_brackets = set(bracket_map.values())
    close_brackets = set(bracket_map.keys())

    stack = []  # зберігає кортежі (символ, індекс)
    invalid_positions = []

    for index, char in enumerate(text):
        if char in open_brackets:
            stack.append((char, index))
        elif char in close_brackets:
            if stack and stack[-1][0] == bracket_map[char]:
                stack.pop()
            else:
                invalid_positions.append(index)

    # Відкриваючі дужки, для яких не знайшлося закриваючих
    for _, index in stack:
        invalid_positions.append(index)

    if invalid_positions:
        invalid_positions.sort()
        positions_str = ", ".join(map(str, invalid_positions))

        # Формування візуального підкреслення під невалідними дужками
        markers = [" "] * len(text)
        for pos in invalid_positions:
            markers[pos] = "^"
        visual_highlight = "".join(markers)

        raise ValueError(
            f"Дужки незбалансовані на позиціях {positions_str}\n"
            f"{text}\n"
            f"{visual_highlight}"
        )

    return True


def main():
    user_input = input("Введіть строку: ")
    try:
        if validate_brackets(user_input):
            print("Строка валідна")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
