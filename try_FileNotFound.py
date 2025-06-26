try:
    f=open('file.txt')
except FileNotFoundError:
    print("File not found,Try again")
except NameError:
    print("Invaild name")