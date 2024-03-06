num = 65765

def hex_number(number: int, mod: int = 16) -> str:
    result = ''
    while number != 0:
        temp = number % mod if (number % mod) < 10 else chr(number % mod + 87)
        result = str(temp) + result
        number //= mod
    return result.upper()

h = hex(num)


print(f"Шестнадцатеричное представление числа: {hex_number(num)}" )
print(f'Проверка результата: {h}')
