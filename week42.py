email = input("Email: ")
if email.endswith("@newton.ac.th") and "." in (email.split("@"))[0]:
    exit("Valid")
print("Invalid")
