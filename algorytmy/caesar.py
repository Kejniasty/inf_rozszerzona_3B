def caesar(character, key):
    n = ord(character)
    n += key
    if character.islower() and n>122 or character.isupper() and n>90:
        n -= 26
    return chr(n)

word = "Informatyka"
encrypted = ""
key = 3

for i in word:
    encrypted += caesar(i, key)
    
print(encrypted)
