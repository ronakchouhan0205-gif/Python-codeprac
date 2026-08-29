username = input("Enter your name: ")
username = username.strip()

password = input("Enter you password: ")
password = password.strip()

balance = input("Enter account balance: ")
balance = float(balance)

has_length = len(password)>=8
has_digit = not password.isalpha() 
has_upper = password != password.lower()
has_special = not password.isalnum()

score = has_length + has_digit + has_upper + has_special 

if score ==4:
    password_strength = "Strong"
elif score >=2:
    password_strength = "Medium"
else:
    password_strength = "Weak"

print(password_strength)

if " " in username or not username.isalnum():
    username_valid = False
    rejection_username = "invalid"
else:
    username_valid = True 
    cleaned_username = username.lower()

print(username_valid)

if password_strength == "Weak" or not username_valid:
    print("Login rejected")
else:
    masked_password = password[:2] + "******"
    print(f"{'Username'}: {username}")
    print(f"{'Masked password'}: {masked_password}")
    print(f"{'Password strength'}: {password_strength}")
    print(f"{'balance'}: {balance:.2f}")
