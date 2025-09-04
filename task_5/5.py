#5 შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან \[1,2,3,4,5] (itertools-ის გამოყენებით)

from itertools import permutations
print(list(permutations([1,2,3,4,5], 3)))
