text = ""
while (True):
    text = input("hi, who are you :")
    text = text.strip().upper()

    if text.isdigit():
        print("pleas enter a text not enter number")
    else:
        if text.startswith("HELLO"):
            print("the text stared by hello")
        if text.endswith("HACK"):

            print("to text has hack ")
        if text.endswith("HACK"):
            text=text.replace("A", "U")
            print(text)

        if text == "EXIT":
            break
