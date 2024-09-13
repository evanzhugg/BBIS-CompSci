# Hashmap Values
map = {
    10: "A", "A": 10,
    11: "B", "B": 11,
    12: "C", "C": 12,
    13: "D", "D": 13,
    14: "E", "E": 14,
    15: "F", "F": 15
}

def dectohex(num):
    if num == 0:
        return "0"
    hex_list = []
    while num > 0:
        val = num % 16
        if val > 9:
            val = map[val]
        hex_list.append(str(val))
        num = num // 16
    hex_list.reverse()
    return ''.join(hex_list)

def hextodec(hex_str):
    hex_str = hex_str.upper()
    decimal_value = 0
    length = len(hex_str)
    for i in range(length):
        digit = hex_str[length - 1 - i]
        if digit in map:
            value = map[digit]
        else:
            value = int(digit)
        decimal_value += value * (16 ** i)
    return decimal_value

# test
# choice = input("16 to 10 (1) or 10 to 16 (2): ")
# if choice == "1":
#     hex_number = input("Enter a hexadecimal number: ")
#     print(hextodec(hex_number))
# elif choice == "2":
#     decimal_number = int(input("Enter a decimal number: "))
#     print(dectohex(decimal_number))
# else:
#     print("Invalid choice")