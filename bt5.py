with open("./question-bank.txt", "r") as file:
    s = file.read()
    global a
    a = s.strip().split("\n")

for i in range(len(a)):
    a[i] = a[i].split(",")
    a[i][1] = int(a[i][1])

point = 0
max_point = len(a)

for i in a:
    ans = int(input(f"{i[0]}"))
    if ans == i[1]:
        point += 1

print(f"== You get {point}/{max_point} points ==")
