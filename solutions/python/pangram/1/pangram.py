def is_pangram(sentence):
    letters = set()

    for char in sentence.lower():
        if char.isalpha():
            letters.add(char)

    return len(letters) == 26