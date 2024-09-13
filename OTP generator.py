import random
print("Welcome to my OTP generator program. Let's get started.")
otp=""
while True:
    length=int(input("How many digits do you want for OTP ?\n"))
    if length<=0:
        print("Invalid operation. Try again.")
        continue
    else:
        for _ in range(length):
            otp+=str(random.randint(0,9))
        print(f"Your {length} digit OTP code is {otp}")
        break
print("Don't share your otp code with anyone.\nThank you for using my program. Bye !!!!")