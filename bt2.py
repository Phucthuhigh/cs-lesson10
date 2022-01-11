file_input = input("Input file name: ")
try:
    with open(f"./{file_input}", "r") as file:
        s = file.read()
        print(f"File content:\n{s}")
except:
    print("File not found.")
