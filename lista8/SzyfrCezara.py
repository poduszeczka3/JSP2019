def crypting(text,s,decipher=False):
    key = "mnbvcxzasdfghjklpoiuytrewq"; key += key.upper(); key = list(key)
    result = ""
    if decipher: s *= -1
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
         # Encrypt uppercase characters in plain text
      
        if char in key:
            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result