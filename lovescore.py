print("Welcome to Love Score Calculator")
name1 = input("Enter your name -> \n")
name2 = input("Enter her/his name -> \n")
name1 = name1.lower()
name2 = name2.lower()
first = 0
first += (name1.count('t') + name2.count('t')) % 10
first += (name1.count('r') + name2.count('r')) % 10
first += (name1.count('u') + name2.count('u')) % 10
first += (name1.count('e') + name2.count('e')) % 10
second = 0
second += (name1.count('l') + name2.count('l')) % 10
second += (name1.count('o') + name2.count('o')) % 10
second += (name1.count('v') + name2.count('v')) % 10
second += (name1.count('e') + name2.count('e')) % 10
lovescore = (10*first + second)
if lovescore >= 90:
    print(f"{lovescore} Wow you two are like coke and mentos together!")
elif lovescore <= 90 and lovescore >= 50:
    print(f"{lovescore} You two are good to go!")
else :
    print(f"Your love is {lovescore}")

