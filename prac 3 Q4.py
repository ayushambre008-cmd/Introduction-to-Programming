age = int(input("Enter your age:" ))

nationality = input("Enter your nationality: ")

if age >= 18:
    if nationality.lower() == "indian":
        print("Eligible to vote.")
    else:
        print("Not Eligible to vote(Only Indian citizens can vote).")
else:
    print("Not Eligible to vote (Age must be 18 or above).")

          
