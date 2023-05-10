def main():
# Ask user for greeting and clean whitespaces in output

    Greeting=input("Greeting: ").strip()

    if Greeting.startswith("Hello"):
        print("$0")
    elif Greeting.startswith("H"):
        print("$20")
    else:
        print("$100")

main()
