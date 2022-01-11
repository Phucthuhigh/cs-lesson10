with open("./names.txt", "r") as file:
    print("List of names:")
    s = file.readline()
    while (s != ""):
        print(f"- {s}", end="")
        s = file.readline()
