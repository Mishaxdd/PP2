#1
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
#2
prices_usd = [10, 50, 100]
prices_rub = list(map(lambda x: x * 90, prices_usd))
#3
users = [{"name": "Ali", "id": 1}, {"name": "Bob", "id": 2}]
names = list(map(lambda u: u["name"], users))
#4
logins = ["admin", "user1", "guest"]
emails = list(map(lambda l: l + "@company.com", logins))
#5
floats = [3.1415, 2.718, 1.618]
rounded = list(map(lambda n: round(n, 2), floats))