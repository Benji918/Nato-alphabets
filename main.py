import pandas as pd

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_read = pd.read_csv('nato_phonetic_alphabet.csv').to_dict()
nato_dic = {row.letter: row.code for(index, row) in pd.DataFrame(nato_read).iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input('Enter your name :').upper()
user_letters = [letter for letter in user_name]
phonetic = [nato_dic[letter] for letter in user_letters if letter in nato_dic.keys()]
print(phonetic)
