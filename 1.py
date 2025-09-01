#1 დაწერეთ პაროლის გენერატორი.
#დავალების შესრულებაში დაგეხმარებათ: random მოდული, while ან for ციკლი, list,
#სტრიქონის ფორმატირება.
#input ის მეშვეობით უნდა შეგვეძლოს მითითება რა სიგრძის პაროლი გვინდა და რა
#სიმბოლეობიდან გენერირდება იგი: პაროლის სიგრძეს ირჩევს მომხმარებელი, უნდა თუ
#არა სიმბოლოები, რიცხვები, დიდი/პატარა ასოები (ლათინურად) თუ ქართულს შემოიტანს
#უნდა დაუწერო რომ “შეიყვანე მხოლოდ ლათინური ასოები”


import random
import string

user_input = {
        "length": None,
        "symbol_uppercase": None, 
        "symbol_lowercase": None,
        "special_characters": None,
        "numbers": None,
      #  "symbols": None
        }

def ask_bool(variable_name, input_text):
    if user_input[variable_name] is None:
      user_input_uppercase = input(input_text).lower()
      if user_input_uppercase[0] == 'y':
        user_input[variable_name] = True
      elif user_input_uppercase[0] == 'n':
           user_input[variable_name] = False

def info_check():
    pass

while True:
    if user_input['length'] is None:
      user_input_length = int(input("length?"))
      if user_input_length > 0:
        user_input['length'] = user_input_length
      else: continue
    print(str(user_input))
    ask_bool(variable_name='symbol_uppercase', input_text='Do you want uppercase in password? Yes/No: ')
    if user_input['symbol_uppercase'] is None: continue
    ask_bool(variable_name='symbol_lowercase', input_text='Do you want lowercase in password? Yes/No: ')
    if user_input['symbol_lowercase'] is None: continue
    ask_bool(variable_name='special_characters', input_text='Do you want special characters in password? Yes/No: ')
    if user_input['special_characters'] is None: continue
    ask_bool(variable_name='numbers', input_text='Do you want numbers in password? Yes/No: ')
    if user_input['numbers'] is None: continue



    while user_input['symbols'] is None:
        should_break = False
        user_input_symbols = input('Type symbols: ').lower()
        for s in user_input_symbols:
            if s not in string.ascii_lowercase:
                should_break = True
                print("Enter Latin Symbols only!")
                break
        if not should_break:
            user_input['symbols'] = user_input_symbols
        else:
            break

    print('zuma')
