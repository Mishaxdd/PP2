#1
add = lambda a, b, c: a + b + c
print(add(5, 10, 15))
#2
is_even = lambda x: x % 2 == 0
print(is_even(44))
#3
get_status = lambda score: "Pass" if score >= 50 else "Fail"
print(get_status(65))
#3
power = lambda base, exp: base ** exp
print(power(2, 10))
#5
clean_text = lambda s: s.strip().lower()
print(clean_text("  PYTHON  "))