count = 0


def greet():
    global count
    count = count + 1
    print(f"{count}: greetings")
    greet()
    print("done")


greet()
