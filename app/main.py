# from PyQt5 import QtWidgets
# import sys
# from encryption_methods.vigenere.vigenere import create_alphabet, create_lines, encrypt_passage, decrypt_passage, clean_input

# class CipherApp(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Obfuscate')

#         # Labels
#         self.key1_label = QtWidgets.QLabel('First Key:')
#         self.key2_label = QtWidgets.QLabel('Second Key:')
#         self.passage_label = QtWidgets.QLabel('Passage:')
#         self.alphabet_label = QtWidgets.QLabel('Alphabet:')
#         self.lines_label = QtWidgets.QLabel('Lines:')
#         self.result_label = QtWidgets.QLabel('Result:')

#         # Inputs
#         self.key1_entry = QtWidgets.QLineEdit(self)
#         self.key2_entry = QtWidgets.QLineEdit(self)
#         self.passage_entry = QtWidgets.QLineEdit(self)

#         # Text areas for alphabet, lines, and result
#         self.alphabet_display = QtWidgets.QTextEdit(self)
#         self.alphabet_display.setReadOnly(True)
#         self.alphabet_display.setFixedHeight(30)

#         self.lines_display = QtWidgets.QTextEdit(self)
#         self.lines_display.setReadOnly(True)
#         self.lines_display.setFixedHeight(150)

#         self.result_display = QtWidgets.QTextEdit(self)
#         self.result_display.setReadOnly(True)
#         self.result_display.setFixedHeight(30)

#         # Set fixed width to ensure same length
#         fixed_width = 400
#         self.alphabet_display.setFixedWidth(fixed_width)
#         self.lines_display.setFixedWidth(fixed_width)
#         self.result_display.setFixedWidth(fixed_width)

#         # Buttons
#         self.encrypt_button = QtWidgets.QPushButton('Encrypt', self)
#         self.decrypt_button = QtWidgets.QPushButton('Decrypt', self)

#         self.encrypt_button.setFixedHeight(30)
#         self.decrypt_button.setFixedHeight(30)

#         self.encrypt_button.clicked.connect(self.encrypt)
#         self.decrypt_button.clicked.connect(self.decrypt)

#         # Layout
#         grid = QtWidgets.QGridLayout()
#         grid.setSpacing(10)

#         grid.addWidget(self.key1_label, 1, 0)
#         grid.addWidget(self.key1_entry, 1, 1, 1, 2)

#         grid.addWidget(self.key2_label, 2, 0)
#         grid.addWidget(self.key2_entry, 2, 1, 1, 2)

#         grid.addWidget(self.passage_label, 3, 0)
#         grid.addWidget(self.passage_entry, 3, 1, 1, 2)

#         grid.addWidget(self.encrypt_button, 4, 1)
#         grid.addWidget(self.decrypt_button, 4, 2)

#         grid.addWidget(self.alphabet_label, 5, 0)
#         grid.addWidget(self.alphabet_display, 5, 1, 1, 2)

#         grid.addWidget(self.lines_label, 6, 0)
#         grid.addWidget(self.lines_display, 6, 1, 1, 2)

#         grid.addWidget(self.result_label, 7, 0)
#         grid.addWidget(self.result_display, 7, 1, 1, 2)

#         self.setLayout(grid)
#         self.show()

#     def encrypt(self):
#         key1 = clean_input(self.key1_entry.text())
#         key2 = clean_input(self.key2_entry.text())
#         passage = clean_input(self.passage_entry.text())
#         my_alphabet = create_alphabet(key1)
#         my_lines = create_lines(key2, my_alphabet)
#         encrypted_passage = encrypt_passage(passage, my_alphabet, my_lines, key2)
#         self.result_display.setText(''.join(encrypted_passage))
#         self.display_alphabet_and_lines(my_alphabet, my_lines)

#     def decrypt(self):
#         key1 = clean_input(self.key1_entry.text())
#         key2 = clean_input(self.key2_entry.text())
#         passage = clean_input(self.passage_entry.text())
#         my_alphabet = create_alphabet(key1)
#         my_lines = create_lines(key2, my_alphabet)
#         decrypted_passage = decrypt_passage(passage, my_alphabet, my_lines, key2)
#         self.result_display.setText(''.join(decrypted_passage))
#         self.display_alphabet_and_lines(my_alphabet, my_lines)

#     def display_alphabet_and_lines(self, alphabet, lines):
#         self.alphabet_display.setText(''.join(alphabet))
#         lines_text = '\n'.join([''.join(line) for line in lines])
#         self.lines_display.setText(lines_text)

# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     ex = CipherApp()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()
from PyQt5 import QtWidgets
import sys
from encryption_methods.vigenere.vigenere import create_alphabet, create_lines, encrypt_passage, decrypt_passage, clean_input

class CipherApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Obfuscate')

        # Labels
        self.method_label = QtWidgets.QLabel('Encryption Method:')
        self.key1_label = QtWidgets.QLabel('First Key:')
        self.key2_label = QtWidgets.QLabel('Second Key:')
        self.passage_label = QtWidgets.QLabel('Passage:')
        self.alphabet_label = QtWidgets.QLabel('Alphabet:')
        self.lines_label = QtWidgets.QLabel('Lines:')
        self.result_label = QtWidgets.QLabel('Result:')

        # ComboBox for encryption method selection
        self.method_combo = QtWidgets.QComboBox(self)
        self.method_combo.addItem('Vigenere')  # Add your encryption methods here
        # self.method_combo.addItem('OtherMethod')  # Example for adding another method

        # Inputs
        self.key1_entry = QtWidgets.QLineEdit(self)
        self.key2_entry = QtWidgets.QLineEdit(self)
        self.passage_entry = QtWidgets.QLineEdit(self)

        # Text areas for alphabet, lines, and result
        self.alphabet_display = QtWidgets.QTextEdit(self)
        self.alphabet_display.setReadOnly(True)
        self.alphabet_display.setFixedHeight(30)

        self.lines_display = QtWidgets.QTextEdit(self)
        self.lines_display.setReadOnly(True)
        self.lines_display.setFixedHeight(150)

        self.result_display = QtWidgets.QTextEdit(self)
        self.result_display.setReadOnly(True)
        self.result_display.setFixedHeight(75)

        # Set fixed width to ensure same length
        fixed_width = 400
        self.alphabet_display.setFixedWidth(fixed_width)
        self.lines_display.setFixedWidth(fixed_width)
        self.result_display.setFixedWidth(fixed_width)

        # Buttons
        self.encrypt_button = QtWidgets.QPushButton('Encrypt', self)
        self.decrypt_button = QtWidgets.QPushButton('Decrypt', self)

        self.encrypt_button.setFixedHeight(30)
        self.decrypt_button.setFixedHeight(30)

        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)

        # Layout
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.method_label, 0, 0)
        grid.addWidget(self.method_combo, 0, 1, 1, 2)

        grid.addWidget(self.key1_label, 1, 0)
        grid.addWidget(self.key1_entry, 1, 1, 1, 2)

        grid.addWidget(self.key2_label, 2, 0)
        grid.addWidget(self.key2_entry, 2, 1, 1, 2)

        grid.addWidget(self.passage_label, 3, 0)
        grid.addWidget(self.passage_entry, 3, 1, 1, 2)

        grid.addWidget(self.encrypt_button, 4, 1)
        grid.addWidget(self.decrypt_button, 4, 2)

        grid.addWidget(self.alphabet_label, 5, 0)
        grid.addWidget(self.alphabet_display, 5, 1, 1, 2)

        grid.addWidget(self.lines_label, 6, 0)
        grid.addWidget(self.lines_display, 6, 1, 1, 2)

        grid.addWidget(self.result_label, 7, 0)
        grid.addWidget(self.result_display, 7, 1, 1, 2)

        self.setLayout(grid)
        self.show()

    def encrypt(self):
        method = self.method_combo.currentText()
        if method == 'Vigenere':
            self.encrypt_vigenere()
        # Add elif branches for other methods

    def decrypt(self):
        method = self.method_combo.currentText()
        if method == 'Vigenere':
            self.decrypt_vigenere()
        # Add elif branches for other methods

    def encrypt_vigenere(self):
        key1 = clean_input(self.key1_entry.text())
        key2 = clean_input(self.key2_entry.text())
        passage = clean_input(self.passage_entry.text())
        my_alphabet = create_alphabet(key1)
        my_lines = create_lines(key2, my_alphabet)
        encrypted_passage = encrypt_passage(passage, my_alphabet, my_lines, key2)
        self.result_display.setText(''.join(encrypted_passage))
        self.display_alphabet_and_lines(my_alphabet, my_lines)

    def decrypt_vigenere(self):
        key1 = clean_input(self.key1_entry.text())
        key2 = clean_input(self.key2_entry.text())
        passage = clean_input(self.passage_entry.text())
        my_alphabet = create_alphabet(key1)
        my_lines = create_lines(key2, my_alphabet)
        decrypted_passage = decrypt_passage(passage, my_alphabet, my_lines, key2)
        self.result_display.setText(''.join(decrypted_passage))
        self.display_alphabet_and_lines(my_alphabet, my_lines)

    def display_alphabet_and_lines(self, alphabet, lines):
        self.alphabet_display.setText(''.join(alphabet))
        lines_text = '\n'.join([''.join(line) for line in lines])
        self.lines_display.setText(lines_text)

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = CipherApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
