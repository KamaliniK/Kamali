#CREDIT/DEBIT CARD VALIDATION CHECKING USING LUHN'S ALGORITHM IN PYTHON
card = input("ENTER  YOUR CARD NUMBER IN THE FORMAT XXXXXXXXXXXXXXXX:")
sum1 = 0
sum2 = 0
for i in range(len(card) - 1, -1, -2):
    sum1 += int(card[i])
for i in range(len(card) - 2, -1, -2):
    n = int(card[i]) * 2
    if n >= 10:
        n = str(n)
        sum2 += int(n[0]) + int(n[1])
    else:
        sum2 += n
total = str(sum1 + sum2)
valid = int(total) % 10
#int(total[len(total) - 1])
if valid == 0:
    print("valid")
else:
    print("invalid")
#-------------------------------------------------------------------------------
