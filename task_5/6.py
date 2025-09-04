#6 მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე
#მაგალითი: X, Y, Z, XY, XZ, YZ, XYZ უნდა მივიღოთ მსგავსი შედეგი.
from itertools import permutations

symbols = "XYZ"
num = 1

while num <= len(symbols):
    for perm in permutations(symbols, num):
        print(perm)
    num += 1
