"""
Create a program that prompts the user to input their age, and then prints out their age category
based on the following criteria:

If the user is less than 2 years old,the program should output "You are a baby.".
If the user is between 2 and 12 years old, the program should output "You are a child.".
If the user is between 13 and 19 years old, the program should output "You are a teenager.".
If the user is 20 years old or older, the program should output "You are an adult.".
"""


def main():
    """Find age category."""
    age = int(input("Enter your age: \n"))
    if age < 2:
        print("You are a baby.")


if __name__ == "__main__":
    print("Age category detector")  # color this caption
    main()
