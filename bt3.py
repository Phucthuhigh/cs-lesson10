print("== Input file content below ==")

a = []
s = input("")
while (s != ""):
    a.append(s)
    s = input("")

with open("./user-inputs.txt", "w") as file:
    txt = "\n".join(a)
    file.write(txt)

print("== Input recorded in user-inputs.txt ==")
