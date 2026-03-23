def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            # Decide base (A or a)
            base = ord('A') if char.isupper() else ord('a')
            
            # Shift character
            shifted = (ord(char) - base + key) % 26 + base
            
            result += chr(shifted)
        else:
            # Keep punctuation/space same
            result += char

    return result