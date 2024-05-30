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
from encryption_methods.enigma.enigma import encode as enigma_encode

# class CipherApp(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Obfuscate')

#         # Labels
#         self.method_label = QtWidgets.QLabel('Encryption Method:')
#         self.key1_label = QtWidgets.QLabel('First Key:')
#         self.key2_label = QtWidgets.QLabel('Second Key:')
#         self.passage_label = QtWidgets.QLabel('Passage:')
#         self.alphabet_label = QtWidgets.QLabel('Alphabet:')
#         self.lines_label = QtWidgets.QLabel('Lines:')
#         self.result_label = QtWidgets.QLabel('Result:')

#         # ComboBox for encryption method selection
#         self.method_combo = QtWidgets.QComboBox(self)
#         self.method_combo.addItem('Vigenere')  # Add your encryption methods here
#         # self.method_combo.addItem('OtherMethod')  # Example for adding another method

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
#         self.result_display.setFixedHeight(75)

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

#         grid.addWidget(self.method_label, 0, 0)
#         grid.addWidget(self.method_combo, 0, 1, 1, 2)

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
#         method = self.method_combo.currentText()
#         if method == 'Vigenere':
#             self.encrypt_vigenere()
#         # Add elif branches for other methods

#     def decrypt(self):
#         method = self.method_combo.currentText()
#         if method == 'Vigenere':
#             self.decrypt_vigenere()
#         # Add elif branches for other methods

#     def encrypt_vigenere(self):
#         key1 = clean_input(self.key1_entry.text())
#         key2 = clean_input(self.key2_entry.text())
#         passage = clean_input(self.passage_entry.text())
#         my_alphabet = create_alphabet(key1)
#         my_lines = create_lines(key2, my_alphabet)
#         encrypted_passage = encrypt_passage(passage, my_alphabet, my_lines, key2)
#         self.result_display.setText(''.join(encrypted_passage))
#         self.display_alphabet_and_lines(my_alphabet, my_lines)

#     def decrypt_vigenere(self):
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


class CipherApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Obfuscate')

        # Create the stacked widget
        self.stacked_widget = QtWidgets.QStackedWidget(self)

        # Create Vigenere page
        self.vigenere_page = self.create_vigenere_page()
        self.stacked_widget.addWidget(self.vigenere_page)

        # Create Enigma page
        self.enigma_page = self.create_enigma_page()
        self.stacked_widget.addWidget(self.enigma_page)

        # ComboBox for encryption method selection
        self.method_combo = QtWidgets.QComboBox(self)
        self.method_combo.addItem('Vigenere')
        self.method_combo.addItem('Enigma')
        self.method_combo.currentIndexChanged.connect(self.switch_page)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.method_combo)
        main_layout.addWidget(self.stacked_widget)

        self.setLayout(main_layout)
        self.show()

    def create_vigenere_page(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()

        # Labels
        # method_label = QtWidgets.QLabel('Encryption Method:')
        key1_label = QtWidgets.QLabel('First Key:')
        key2_label = QtWidgets.QLabel('Second Key:')
        passage_label = QtWidgets.QLabel('Passage:')
        alphabet_label = QtWidgets.QLabel('Alphabet:')
        lines_label = QtWidgets.QLabel('Lines:')
        result_label = QtWidgets.QLabel('Result:')

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

        self.encrypt_button.clicked.connect(self.encrypt_vigenere)
        self.decrypt_button.clicked.connect(self.decrypt_vigenere)

        # Layout
        # layout.addWidget(method_label, 0, 0)
        layout.addWidget(self.key1_entry, 1, 1, 1, 2)
        layout.addWidget(key1_label, 1, 0)
        layout.addWidget(self.key2_entry, 2, 1, 1, 2)
        layout.addWidget(key2_label, 2, 0)
        layout.addWidget(self.passage_entry, 3, 1, 1, 2)
        layout.addWidget(passage_label, 3, 0)
        layout.addWidget(self.encrypt_button, 4, 1)
        layout.addWidget(self.decrypt_button, 4, 2)
        layout.addWidget(alphabet_label, 5, 0)
        layout.addWidget(self.alphabet_display, 5, 1, 1, 2)
        layout.addWidget(lines_label, 6, 0)
        layout.addWidget(self.lines_display, 6, 1, 1, 2)
        layout.addWidget(result_label, 7, 0)
        layout.addWidget(self.result_display, 7, 1, 1, 2)

        widget.setLayout(layout)
        return widget

    def create_enigma_page(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()

        # Labels
        rotor_label = QtWidgets.QLabel('Rotors:')
        reflector_label = QtWidgets.QLabel('Reflector:')
        ring_settings_label = QtWidgets.QLabel('Ring Settings:')
        ring_positions_label = QtWidgets.QLabel('Ring Positions:')
        plugboard_label = QtWidgets.QLabel('Plugboard:')
        passage_label = QtWidgets.QLabel('Passage:')
        result_label = QtWidgets.QLabel('Result:')

        # Inputs
        self.rotor_entry = QtWidgets.QLineEdit(self)
        self.rotor_entry.setText("I II III")  # Default value

        self.reflector_entry = QtWidgets.QLineEdit(self)
        self.reflector_entry.setText("UKW-B")  # Default value

        self.ring_settings_entry = QtWidgets.QLineEdit(self)
        self.ring_settings_entry.setText("ABC")  # Default value

        self.ring_positions_entry = QtWidgets.QLineEdit(self)
        self.ring_positions_entry.setText("DEF")  # Default value

        self.plugboard_entry = QtWidgets.QLineEdit(self)
        self.plugboard_entry.setText("AT BS DE FM IR KN LZ OW PV XY")  # Default value

        self.enigma_passage_entry = QtWidgets.QLineEdit(self)

        # Text area for result
        self.enigma_result_display = QtWidgets.QTextEdit(self)
        self.enigma_result_display.setReadOnly(True)
        self.enigma_result_display.setFixedHeight(75)

        # Set fixed width to ensure same length
        fixed_width = 400
        self.enigma_result_display.setFixedWidth(fixed_width)

        # Button
        self.enigma_process_button = QtWidgets.QPushButton('Encrypt/Decrypt', self)
        self.enigma_process_button.setFixedHeight(30)
        self.enigma_process_button.clicked.connect(self.process_enigma)

        # Layout
        layout.addWidget(rotor_label, 0, 0)
        layout.addWidget(self.rotor_entry, 0, 1, 1, 2)
        layout.addWidget(reflector_label, 1, 0)
        layout.addWidget(self.reflector_entry, 1, 1, 1, 2)
        layout.addWidget(ring_settings_label, 2, 0)
        layout.addWidget(self.ring_settings_entry, 2, 1, 1, 2)
        layout.addWidget(ring_positions_label, 3, 0)
        layout.addWidget(self.ring_positions_entry, 3, 1, 1, 2)
        layout.addWidget(plugboard_label, 4, 0)
        layout.addWidget(self.plugboard_entry, 4, 1, 1, 2)
        layout.addWidget(passage_label, 5, 0)
        layout.addWidget(self.enigma_passage_entry, 5, 1, 1, 2)
        layout.addWidget(self.enigma_process_button, 6, 1, 1, 2)
        layout.addWidget(result_label, 7, 0)
        layout.addWidget(self.enigma_result_display, 7, 1, 1, 2)

        widget.setLayout(layout)
        return widget

    def switch_page(self, index):
        self.stacked_widget.setCurrentIndex(index)

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

    def process_enigma(self):
        rotors = tuple(self.rotor_entry.text().split())
        reflector = self.reflector_entry.text()
        ring_settings = self.ring_settings_entry.text()
        ring_positions = self.ring_positions_entry.text()
        plugboard = self.plugboard_entry.text()
        passage = self.enigma_passage_entry.text().upper()
        processed_passage = enigma_encode(passage, rotors, reflector, ring_settings, ring_positions, plugboard)
        self.enigma_result_display.setText(processed_passage)

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
