import re

alphabet = list('abcdefghijklmnopqrstuvwxyz')

def create_alphabet(key1_string):
    top_alphabet = list(alphabet)
    for counter, letter in enumerate(key1_string):
        top_alphabet.remove(letter)
        top_alphabet.insert(counter, letter)
    return top_alphabet

def create_lines(key2_string, my_alphabet):
    list_of_alphabets = []
    for letter in key2_string:
        index = my_alphabet.index(letter) + 1
        line_alphabet = [my_alphabet[(index + i) % len(my_alphabet)] for i in range(26)]
        list_of_alphabets.append(line_alphabet)
    return list_of_alphabets

def decrypt_passage(passage, my_alphabet, my_lines, key2_string):
    decrypted_passage = []
    for counter, letter in enumerate(passage):
        our_row = my_lines[counter % len(key2_string)]
        index = our_row.index(letter) + 1
        decrypted_passage.append(my_alphabet[index % len(my_alphabet)])
    return ''.join(decrypted_passage)

def encrypt_passage(passage, my_alphabet, my_lines, key2_string):
    encrypted_passage = []
    for counter, letter in enumerate(passage):
        index = my_alphabet.index(letter) - 1
        our_row = my_lines[counter % len(key2_string)]
        encrypted_passage.append(our_row[index])
    return ''.join(encrypted_passage)

def clean_input(text):
    return re.sub(r'\s+', '', text.lower())
