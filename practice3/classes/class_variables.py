# 1
class School:
    name = "ABC School"

print(School.name)
# 2
class Game:
    players = 0

Game.players += 1
print(Game.players)
# 3
class Company:
    employees = 50

c1 = Company()
c2 = Company()
print(c1.employees, c2.employees)
# 4
class Config:
    VERSION = "1.0.0"

print(Config.VERSION)
# 5
class Bank:
    interest_rate = 0.05

print(Bank.interest_rate)