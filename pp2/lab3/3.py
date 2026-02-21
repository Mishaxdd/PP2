w2n = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}
back_to_word = {"0":"ZER", "1":"ONE", "2":"TWO", "3":"THR", "4":"FOU", "5":"FIV", "6":"SIX", "7":"SEV", "8":"EIG", "9":"NIN"}

s = input().strip()

if "+" in s:
    parts = s.split("+")
    op = "+"
elif "-" in s:
    parts = s.split("-")
    op = "-"
else:
    parts = s.split("*")
    op = "*"

left_str = parts[0]
num1_str = ""
for i in range(0, len(left_str), 3):
    triplet = left_str[i:i+3]
    num1_str += w2n[triplet]
num1 = int(num1_str)

right_str = parts[1]
num2_str = ""
for i in range(0, len(right_str), 3):
    triplet = right_str[i:i+3]
    num2_str += w2n[triplet]
num2 = int(num2_str)

if op == "+":
    res = num1 + num2
elif op == "-":
    res = num1 - num2
else:
    res = num1 * num2

final_res = str(res)
for digit in final_res:
    if digit == "-":
        continue
    print(back_to_word[digit], end="")
print()