print("Hello")

name = input("name >>")

print(f"your name is {name}")

for n in range(1,10):
    if n%2 == 0:
        print("Gerade")
    else:
        print("Ungerade")

def ask_age():
    name = input("what is your age? >> ")
    return name

print(ask_age())
