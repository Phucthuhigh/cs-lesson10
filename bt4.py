import datetime

file_name = "input-logs.txt"

print("== Input file content below ==")
a = []
s = input("")
now = datetime.datetime.now()
while (s != ""):
    a.append(s)
    s = input("")

try:
    global exist
    with open(f"./{file_name}", "r") as file:
        exist = True
        s = file.read()
        if (s == ""):
            exist = False
except:
    exist = False

with open(f"./{file_name}", "a") as file:
    if exist:
        file.write("\n")
    file.write(f"== Inputs at {now} ==\n")
    for i in a:
        file.write(f"{i}\n")

print(f"== Input recorded in {file_name} ==")
