# import re

# alphabet = list('abcdefghijklmnopqrstuvwxyz')

# def create_alphabet(key1_string):
#     top_alphabet = list(alphabet)
#     for counter, letter in enumerate(key1_string):
#         top_alphabet.remove(letter)
#         top_alphabet.insert(counter, letter)
#     return top_alphabet

# def create_lines(key2_string, my_alphabet):
#     list_of_alphabets = []
#     for letter in key2_string:
#         index = my_alphabet.index(letter) + 1
#         line_alphabet = [my_alphabet[(index + i) % len(my_alphabet)] for i in range(26)]
#         list_of_alphabets.append(line_alphabet)
#     return list_of_alphabets

# def decrypt_passage(passage, my_alphabet, my_lines, key2_string):
#     decrypted_passage = []
#     for counter, letter in enumerate(passage):
#         our_row = my_lines[counter % len(key2_string)]
#         index = our_row.index(letter) + 1
#         decrypted_passage.append(my_alphabet[index % len(my_alphabet)])
#     return ''.join(decrypted_passage)

# def encrypt_passage(passage, my_alphabet, my_lines, key2_string):
#     encrypted_passage = []
#     for counter, letter in enumerate(passage):
#         index = my_alphabet.index(letter) - 1
#         our_row = my_lines[counter % len(key2_string)]
#         encrypted_passage.append(our_row[index])
#     return ''.join(encrypted_passage)

# def clean_input(text):
#     return re.sub(r'\s+', '', text.lower())


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
