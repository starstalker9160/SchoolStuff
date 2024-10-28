t = ((), (), ())
n = int(input("How many students? "))

for i in range(n):
    roll = int(input("Enter the roll no. of student " + str(i + 1) + ": "))
    name = input("Enter the name of student " + str(i + 1) + ": ")
    marks = float(input("Enter the marks of student " + str(i + 1) + ": "))

    t = (t[0] + (roll,), t[1], t[2])
    t = (t[0], t[1] + (name,), t[2])
    t = (t[0], t[1], t[2] + (marks,))

topper = []
x = 0
for mark in t[2]:
    if mark == 95:
        topper += [[t[1][x], mark]]
    x += 1

if len(topper) == 0:
    print("No student has gotten 95 marks.")
else:
    for i in topper:
        print(i[0], "has gotten", i[1], "marks.")

print("The tuple is:")
print(t)