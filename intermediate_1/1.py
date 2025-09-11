# #1 მინი-ბიბლიოთეკა
# --------------------
# თქვენი მიზანია შექმნათ „მინი-ბიბლიოთეკის მართვის სისტემა“, სადაც:
# - მომხმარებელს შეუძლია დაამატოს წიგნი (სათაური, ავტორი, წელი)
# - შეინახოს ისინი სიაში
# - მოძებნოს წიგნი სათაურით
# - დაინახოს ყველა წიგნის სია (სათაური + ავტორი)
# დეტალები:
# -----------
# 1. შექმენით წინასწარი "სია" სადაც მოთავსებული იქნება 10 თქვენს მიერ არჩეული წიგნის სახელი/ავტორი და წელი
# 2. მომხმარებელს აქვს საშუალება: წიგნი დაამატოს ამ ფორმატით სახელი/ავტორი და წელი
# 3. მომხმარებელს აქვს საშუალება: ნახოს უკვე არსებული წიგნები რაც ბიბლიოთეკაშია (10 წიგნი)
# 4. აირჩიოს მისთვის სასურველი და გაიტანოს ბიბლიოთეკიდან "წასაკითხად"
# 5. მომხმარებლის მიერ დამატებული წიგნი უნდა დაემატოს ბიბლიოთეკის სიას და მომდევნო გამოძახებაზე 10-ის მაგივრად უნდა გამოჩნდეს 11 და ა.შ. სანამ მომხმარებელი დაამატებს წიგნებს
# 6. ვალიდაცია არაა საჭირო lower/upper და ა.შ. (მომხმარებელს ყოველთვის შეჰყავს სწორი ინფორმაცია)

mini_library = {
    1: {"title": "1984", "author": "George Orwell", "year": 1949},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    3: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    4: {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    5: {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851},
    6: {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "year": 1967},
    7: {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866},
    8: {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    9: {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
    10: {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": "1954–1955"}
}

user_input = input("შეიყვანე რომელი ოპერაციის შესრულება გსურს \nგატანა \nდამატება \nწიგნების სია \nგასვლა\n")

# Print all books
def check_book():
    for key, value in mini_library.items():
        print(f"{value['title']} - {value['author']} ")

# Add book in library
def user_book_add(book_name, book_author, book_year):
    book_number = max(mini_library.keys()) + 1
    mini_library[book_number] = {
        "title": book_name,
        "author": book_author,
        "year": book_year
    }
    print(mini_library)
    book_number += 1

# Take out book from library
def book_take_out(user_book_number):
    if user_book_number <= len(mini_library):
        del mini_library[user_book_number]
        print(mini_library)
    else:
        print("book number out of range")

# Search book by name
def search_book_by_name(book_name):
    for key, value in mini_library.items():
        if value["title"] == book_name:
            return f"Found: {value['title']} - {value['author']} ({value['year']})"
        return "Book not found."


# #2 პროგრამა "21" ქულა
# ---------------------
# წესები:
#
# - დასტა შედგება 52 კარტისაგან - 4 ვარიანტი ("ყვავი" "ჯვარი" "გული" "აგური")
# - 2-დან 10-მდე + Jack + Queen + King + Ace
# - კარტების ღირებულება - 2-10მდე = თავისივე მნიშვნელობა (ანუ 3 = 3, 7 = 7 და ა.შ.) ; J,Q,K = 10 ; Ace = 11 (მარტივი ვარიანტი, უდრის მხოლოდ 11-ს)
# - მოთამაშე და კომპიუტერი იღებენ კარტებს (თავდაპირველად 2-2, შემთხვევითობის პრინციპით)
# - მოთამაშეს შეუძლია აირჩიოს "add" (დამატება) ან "stop" (გაჩერდეს)
# - კომპიუტერი თავის მხრივ იღებს კარტებს მანამ, სანამ ქულა < 17
# - ვინც 21-ს მიუახლოვდება, მაგრამ არ გადააჭარბებს, ის იგებს
#
# თუ მოთამაშე მოიგებს გამოგვაქვს "თქვენ მოიგეთ" თუ კომპიუტერი "თქვენ წააგეთ" ფრეზე ვარიგებთ ხელახლა.
#
# შეგიძლიათ გამოიყენოთ:
# ------------------------
# 1. ციკლები
# 2. პირობითი ოპერატორები
# 3. ფუნქცია
# 4. მოდულები

diamonds = []
hearts = []
spades = []
clubs = []


# #3 ATM Machine
# --------------
#
# პროგრამა მუშაობს როგორც ბანკომატი:
#
# - მომხმარებელს აქვს ანგარიშზე X თანხა რომელსაც წინასწარ ვინახავთ
# - მომხმარებელს შეუძლია შეამოწმოს ბალანსი (ბრძანებით)
# - მომხმარებელს შეუძლია თანხის: "გატანა", "შემოტანა", ბალანსის ნახვა
# - აუცილებელი ვალიდაციები: ვერ უნდა გაიტანოს იმაზე მეტი რაც ანგარიშზე აქვს და ასევე ერთჯერადად ვერ უნდა შეიტანოს 1000ზე მეტი
# - ბანკომატი მუშაობს მხოლოდ ლარზე
# - ყველა ოპერაცია უნდა ჩაიწეროს ლოგერში და შეიხანოს ლოგ ფაილში (გატანა, შემოტანა)
# - მომხმარებელს ყოველთვის შემოჰყავს სწორი ბრძანებები არაა საჭირო ცალკე ვალიდაციების გაწერა
import logging

x = 100
user_input = input("შეიყვანე რომელი ოპერაციის შესრულება გსურს \nგატანა \nშემოტანა \nბალანსის შემოწმება \nგასვლა\n")

def user_check_balance(x):
    print(f"თქვენი ბალანსია {x} ლარი")

def user_add_balance(x,y):
    with open("transactions-in.log", "a") as f:
        if y > 1000:
            msg = "აღნიშნულ თანხას ვერ შემოიტანთ"
            print(msg)
            f.write(msg + "\n")
        else:
            msg = f"თანხა დაემატა თქვენს ბალანს. თქვენი ბალანსია {x + y}"
            print(msg)
            f.write(msg + "\n")
            x + y

def user_withdraw(x, z):
    with open("transactions-out.log", "a") as f:
        if z > x:
            msg = "არასაკმარისი თანხა"
            print(msg)
            f.write(msg + "\n")
        else:
            msg = f"თანხა წარმატებით გაიტანეთ. თქვენს ანგარიშზე დარჩა {x - z}"
            print(msg)
            f.write(msg + "\n")

while True:
        if user_input == "ბალანსის შემოწმება":
            user_check_balance(x)
            break
        elif user_input == "შემოტანა":
            user_add_balance(x,int(input("შეიყვანე თანხა რომლისას შემოტანა გსურს: ")))
            break
        elif user_input == "გატანა":
            user_withdraw(x,int(input("შეიყვანე თანხა რომლისას გამოტანაც გსურს: ")))
            break
        elif user_input == "გასვლა":
            break

# #4 ლატარიის სიმულატორი
# --------------------------
#
# - კომპიუტერი ირჩევს 6 შემთხვევით რიცხვს 1–დან 49-მდე
# - მოთამაშეს შეჰყავს 6 რიცხვი
# - ითვლება, რამდენი დაემთხვა
# - წინასწარ გაწერილია გასათამაშებელი თანხა
# - logging ინახავს ყველა გათამაშებას და შედეგს
# - მომხმარებელს ყოველთვის შემოჰყავს სწორი მნიშვნელობები
#
# --------------------------------------------------------
#
# ლოგიკა:
# 1. 6-6 დამთხვევის შემთხვევაში თამაშდება JACKPOT
# 2. 6-5 დამთხვევის შემთხვევაში JACKPOT-ის თანხას ვაკლებთ 40%-ს
# 3. 6-4 დამთხვევის შემთხვევაში JACKPOT-ის თანხას ვაკლებთ 60%-ს
# 4. 6-3 დამთხვევის შემთხვევაში JACKPOT-ის თანხას ვაკლებთ 80%-ს
# 5. 6-2 და 6-1 დამთხვევის შემთხვევაში მოთამაშე ვერაფერს ვერ იგებს

import random

jackpot = 1000
computer_choice = random.sample(range(1, 50), 6)

user_input = input("შეიყვანეთ 6 რიცხვი: ")
user_choice = []

for i in user_input:
    user_choice.append(int(i))

matches = len(set(user_choice).intersection(set(computer_choice)))

with open("game.log", "a") as f:
    if matches == 6:
        msg = f"თქვენ მოიგეთ JACKPOT: {jackpot}"
        print(msg)
        f.write(msg + "\n")
    elif matches == 5:
        msg = f"დამთხვევა 5. თქვენ მოიგეთ {jackpot - (jackpot * 40 / 100)}"
        print(msg)
        f.write(msg + "\n")
    elif matches == 4:
        msg = f"დამთხვევა 4. თქვენ მოიგეთ {jackpot - (jackpot * 60 / 100)}"
        print(msg)
        f.write(msg + "\n")
    elif matches == 3:
        msg = f"დამთხვევა 3. თქვენ მოიგეთ {jackpot - (jackpot * 80 / 100)}"
        print(msg)
        f.write(msg + "\n")
    elif matches == 2:
        msg = f"დამთხვევა 2. სამწუხაროდ თქვენ ვერ მოიგეთ"
        print(msg)
        f.write(msg + "\n")
    elif matches == 1:
        msg = f"დამთხვევა 1. სამწუხაროდ თქვენ ვერ მოიგეთ"
        print(msg)
        f.write(msg + "\n")
    else:
        msg = f"არ არის დამთხვევა"
        print(msg)
        f.write(msg + "\n")


while True:
    if user_input == "წიგნების სია":
        check_book()
        break
    elif user_input == "დამატება":
        book_name = input("შეიყვანე წიგნის სახელი: ")
        book_author = input("შეიყვანე წიგნის ავტორი: ")
        book_year = input("შეიყვანე წელი: ")
        user_book_add(book_name, book_author, book_year)
        break
    elif user_input == "გატანა":
        search_book_by_name(input(f"შეიყვანე წიგნის სახელი, რომლის გატანაც გსურს {user_input}"))
        break
    elif user_input == "გასვლა":
        break

# #5 რეგისტრაციის სიმულატორი
# -------------------------------
#
# მომხმარებელს ვარეგისტრირებთ ჩვენს ვებ-გვერდზე სადაც არის 4 ველი: "ელ-ფოსტა", "სახელი", "ზედმეტსახელი" და პაროლი
#
# - სახელის გარდა ყველა ველი უკვე შევსებულია, რომელსაც ვინახავთ წინასწარ მაგ: user@mail.com, ... george777 და password123
# - მომხმარებელს შეჰყავს მხოლოდ სახელი, რომელიც აუცილებლად უნდა იყოს ტექსტური ტიპი (ლათინური ასოები და პატარა ასოები)
# - სხვა ნებისმიერი ტიპის მონაცემთა ტიპის შემთხვევაში უნდა გავუტანოთ შესაბამისი შეტყობინება
# - მაგალითი 1: შემოიყვანა: 123 -> "შემოყვანილია რიცხვითი მნიშვნელობა, შემოიტანეთ მხოლოდ string პატარა რეგისტრში"
# - მაგალითი 2: შემოიყვანა: @# -> "შემოყვანილია სიმბოლოები, შემოიტანეთ მხოლოდ string პატარა რეგისტრში" და ა.შ. ყველა შესაძლო ტიპი უნდა განსაზღვროთ
# - ლათინურისგან განსხვავებულს უნდა დაუწეროთ რომ არის სხვა ენა
# - მომხმარებელი თუ შემოიყვანს სტრინგს უნდა დაარეგისტრიროთ და გამოიტანოთ ყველა შენახული მონაცემი:"ელ-ფოსტა", "სახელი", "ზედმეტსახელი" და პაროლი

from string import ascii_lowercase, ascii_uppercase, ascii_letters, punctuation

user_name = input(f"ჩვენს ვებ-გვერდზე რეგისტრაციისთვის, გთხოვთ შემოიყვანოთ სახელი:")
user_email = f"{user_name}@gmail.com"
user_nickname = f"{user_name}777"
user_password = "password123"

while True:
    valid = True
    for i in user_name:
        if i.isdigit():
            print(f"შემოყვანილია რიცხვითი მნიშვნელობა, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")
            valid = False
        elif i in ascii_uppercase:
            print(f"შემოყვანილია მაღალი სიმბოლოების მნიშვნელობა, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")
            valid = False
        elif i in punctuation:
            print(f"შემოიყვანა: @# -> შემოყვანილია სიმბოლოები, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")
            valid = False
        elif i not in ascii_letters:
            print(f"შემოყვანილი string სხვა ენაა. გთხოვთ შემოიყვანოთ ლათინური სიმბოლოები")
            valid = False
    if valid:
        print(f"თქვენი მონაცემებია {user_name}, {user_email}, {user_nickname}, {user_password}")
        break
    else:
        user_name = input("გთხოვთ თავიდან შეიყვანოთ სახელი: ")


