import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("🎮 Welcome to Arpita's Number Guessing Game!")
    print("Maine 1 se 100 ke beech ek number socha hai.")
    print(f"Tumhare paas {max_attempts} chances hain. Best of Luck! 🍀")

    while attempts < max_attempts:
        try:
            guess = int(input("\nApna guess enter karo: "))

            if guess < 1 or guess > 100:
                print("😅 1 se 100 ke beech ka number daalo!")
                continue

            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Thoda bada socho.")
            elif guess > secret_number:
                print("📈 Too high! Thoda chhota socho.")
            else:
                print(f"🎉 Wah! Tumne {attempts} attempts me number guess kar liya!")
                break

            print(f"Remaining chances: {max_attempts - attempts}")

        except ValueError:
            print("😑 Number daalna tha, kuch aur nahi!")

    else:
        print(f"\n💀 Game Over! Number tha: {secret_number}")
        print("Koi baat nahi, agli baar pakka jeetoge! 😄")

guess_the_number()