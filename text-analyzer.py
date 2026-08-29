text = input("Enter your text:\n").strip()

words = text.split()

find_python = 0

for word in words:
    if "python" in word.lower():
        find_python += 1

has_security = "security" in text.lower()

print("========== TEXT ANALYZER ==========\n")
print(f"Characters: {len(text)}")
print(f"Words: {len(words)}")
print(f"Python occurrences: {find_python}")
print(f"Contains security: {has_security}\n")
print(f"Lowercase:\n{text.lower()}\n")
print(f"Reversed:\n{text[::-1]}")
print("\n====================================")
