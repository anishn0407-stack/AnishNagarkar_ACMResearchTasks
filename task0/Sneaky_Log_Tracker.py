import re

s = str(input("Enter your email address = "))
email = r'[a-zA-Z0-9_]+@[a-zA-Z]+\.[a-zA-Z.]+'
txt = re.sub(email, '[HIDDEN]', s)
print("Cleaned mail = ",txt)
