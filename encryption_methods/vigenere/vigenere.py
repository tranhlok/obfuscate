def create_alphabet(key):
    # Create a unique alphabet based on the key
    alphabet = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    remaining_letters = ''.join(sorted(set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - set(alphabet)))
    return alphabet + remaining_letters

def create_lines(key, alphabet):
    # Create the lines for Vigenere table based on the key and alphabet
    key_sequence = [alphabet.index(k) for k in key]
    lines = []
    for shift in key_sequence:
        line = alphabet[shift:] + alphabet[:shift]
        lines.append(line)
    return lines

def clean_input(text):
    return ''.join(filter(str.isalpha, text)).upper()

def encrypt_passage(passage, alphabet, lines, key):
    key_indices = [alphabet.index(k) for k in key]
    result = []
    key_length = len(key)
    for i, char in enumerate(passage):
        if char.isalpha():
            line = lines[i % key_length]
            index = alphabet.index(char)
            result.append(line[index])
        else:
            result.append(char)  # Keep non-alphabet characters unchanged
    return result

def decrypt_passage(passage, alphabet, lines, key):
    key_indices = [alphabet.index(k) for k in key]
    result = []
    key_length = len(key)
    for i, char in enumerate(passage):
        if char.isalpha():
            line = lines[i % key_length]
            index = line.index(char)
            result.append(alphabet[index])
        else:
            result.append(char)  # Keep non-alphabet characters unchanged
    return result
