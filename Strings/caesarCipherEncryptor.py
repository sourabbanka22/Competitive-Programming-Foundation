def caesarCipherEncryptor(string, key):
    # Write your code here.
    key %= 26
    result = []
    for character in string:
        converted = chr(((ord(character) - ord("a") + key) % 26) + ord("a"))
        result.append(converted)
    
    return "".join(result)

print(caesarCipherEncryptor("xyz", 2))