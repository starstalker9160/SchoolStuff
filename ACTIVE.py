s = input(">>> ")
v, c, d, sp, ob = 0, 0, 0, 0, 0
for i in s:
    if i in "0123456789":
        d += 1
    elif i in "aeiou" or i in "AEIOU":
        v += 1
    elif i in "bcdfghjklmnpqrstvwxyz" or i in "BCDFGHJKLMNPQRSTVWXYZ":
        c += 1
    elif i in " ":
        sp += 1
    else:
        ob += 1

while True:
    print("\n")
    print("\t#--------rEeee--------#")
    print("\t|Count number of:     |")
    print("\t|  1. Vowels          |")
    print("\t|  2. Consonants      |")
    print("\t|  3. Digits          |")
    print("\t|  4. Spaces          |")
    print("\t|  5. Special Chars   |")
    print("\t|                     |")
    print("\t|  6. Exit            |")
    print("\t#---------------------#")
    o = int(input("> "))
    if o == 1:
        print(f"\nNo. of vowels is: {v}")
    elif o == 2:
        print(f"\nNo. of consonants is: {c}")
    elif o == 3:
        print(f"\nNo. of digits is: {d}")
    elif o == 4:
        print(f"\nNo. of spaces is: {sp}")
    elif o == 5:
        print(f"\nNo. of special characters is{sp}")
    elif o == 6:
        break
    else:
        print("INVALID INPUT")
