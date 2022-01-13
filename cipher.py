def encrypt(t, a):
    result = ""

    for i in range(len(t)):
        char = t[i]

        if char.isupper():
            result += chr((ord(char) + a - 65) % 26 + 65)

        else:
            result += chr((ord(char) + a - 97) % 26 + 97)
        return result


password = input("Hey enter ur password: ")
shift_pattern = 17

print("Plain Text : " + password)
print("Shift pattern : " + str(shift_pattern))
print("Cipher: " + encrypt(password, shift_pattern))
