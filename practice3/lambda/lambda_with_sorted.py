#1
items = ["apple", "banana", "cherry"]
by_last_letter = sorted(items, key=lambda s: s[-1])
#2
people = [("Ivan", 30), ("Anna", 20), ("Oleg", 25)]
by_age = sorted(people, key=lambda p: p[1])
#3
shop = [{"item": "phone", "price": 500}, {"item": "case", "price": 20}]
expensive_first = sorted(shop, key=lambda x: x["price"], reverse=True)
#4
strings = ["a", "abc", "ab"]
by_length = sorted(strings, key=lambda s: len(s))
#5
mixed_nums = [-100, 5, -20, 50]
by_abs = sorted(mixed_nums, key=lambda x: abs(x))