# 1 შექმენი გენერატორი, რომელიც ტექსტის თითოეულ სიმბოლოს აბრუნებს.
Word = "CODE"
def word_generator(word):
    for i in word:
        yield i

word = word_generator(Word)

for j in word:
    print(j)


