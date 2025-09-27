# #1 SQL დავალება
# გამოიტანე ProductName, CategoryID, Unit, Price ცხრილი- პროდუქტები
# სადაც ფასი მოთავსებული 18-სა და 25-ს შორის
# დაალაგე კლებადობით ფასის მიხედვით

"""
SELECT ProductName, CategoryID, Unit, Price FROM Products
WHERE Price > 18 and Price < 25
ORDER BY PRICE DESC;
"""

#2 SQL დავალება2
# გამოიტანე ყველა ველი, სადაც რაოდენობა ტოლია 15-ის ან 12-ის
# დაალაგე ზრდადობით
# ცხრილი - “OrderDetails”

"""
SELECT * FROM OrderDetails
WHERE Quantity = 12 or Quantity =15
ORDER BY Quantity ASC;
"""

#3 მოცემულია JSON მასივი:
x = '''[
{"id": 1, "price": 50},
{"id": 2, "price": 200},
{"id": 3, "price": 150}
]'''
#ამოიღე მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია.
import json
y = json.loads(x)
print(y)
for prod in y:
    if prod["price"] > 100:
        print(prod)

#4 მოცემულია რთული JSON:
import json

company_employees = '''{
"company": {
"departments": [
{"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
{"name": "HR", "employees": [{"name": "Nino"}]}
]
}
}'''
#ამოიღე ყველა თანამშრომლის სახელი

company_employees_data = json.loads(company_employees)
for department in company_employees_data["company"]["departments"]:
    for employee in department["employees"]:
        print(employee["name"])


names = [employee["name"] for department in company_employees_data["company"]["departments"]
            for employee in department["employees"]]

print(names)
