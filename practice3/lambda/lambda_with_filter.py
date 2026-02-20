#1
numbers = [-10, 5, -2, 0, 8]
positives = list(filter(lambda x: x > 0, numbers))
#2
words = ["cat", "elephant", "dog", "giraffe"]
long_words = list(filter(lambda w: len(w) > 5, words))
#3
staff = [{"user": "A", "is_admin": True}, {"user": "B", "is_admin": False}]
admins = list(filter(lambda s: s["is_admin"], staff))
#4
range_nums = range(1, 20)
div_by_3 = list(filter(lambda x: x % 3 == 0, range_nums))
#5
raw_data = ["hello", "", "world", " ", "python"]
clean_data = list(filter(lambda s: s.strip(), raw_data))