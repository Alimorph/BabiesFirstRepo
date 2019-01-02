def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if sentence.lower().find(letter) == -1:
            return False
    return True
