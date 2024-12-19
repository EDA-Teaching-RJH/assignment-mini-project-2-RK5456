import re  
import csv  
from datetime import datetime  

# I used zyzz greetings since he is my favourite gym bro
def zyzz_greeting(name):
    return f"U mirin brah? Welcome to the zyzz world {name}!"

# email checks
def validate_email(email):
    # Checks if the email format is valid using a regular expression
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"  
    
    # Returns True if the email matches the pattern
    return bool(re.match(pattern, email))  

# Object-Oriented Programming
class User:
    # shows a user with a name, email, and the time they joined
    def __init__(self, name, email):
        if not name:
            # Makes sure the name is provided
            raise ValueError("Missing name")  
        if not validate_email(email):
            # checks the email format
            raise ValueError(f"Invalid email: {email}")  
        self.name = name
        self.email = email
        # Saves the current time
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

    def display_info(self):
        
        # acts as a translator for us
        return f"{self.name} ({self.email}) joined on {self.timestamp}"

    def to_dict(self):
        # Converts user info into a dictionary 
        return {"name": self.name, "email": self.email, "timestamp": self.timestamp}

class GymBro(User):
    # since its now gym based
    def __init__(self, name, email, gym):
        super().__init__(name, email)  
        # Adds gym info
        self.gym = gym  

    def display_info(self):
        # Adds gym info to the user display
        return f"{self.name}, repping {self.gym}, joined on {self.timestamp}"

# File I/O used here which is where data is saved
def save_users_to_file(users, filename="chestbrah_users.csv"):
    # Saves a list of users to a CSV file
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "timestamp", "gym"])
        writer.writeheader()  
        for user in users:
            # Converts user to a dictionary
            row = user.to_dict()  
            row["gym"] = getattr(user, "gym", "N/A")  
            # Saves the row to the file
            writer.writerow(row)  

def load_users_from_file(filename="chestbrah_users.csv"):
    # Loads users from a CSV file
    users = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Creates GymBro if gym info exists, otherwise creates a User
                if row["gym"] != "N/A":
                    users.append(GymBro(row["name"], row["email"], row["gym"]))
                else:
                    users.append(User(row["name"], row["email"]))
    except FileNotFoundError:
        # If the file doesn't exist, no users are loaded
        print(f"No gains yet, file {filename} not found.")
    return users

# Main Program
def main():
    # Main function to manage the program
    print(zyzz_greeting("GymBro"))  
    # List to store users
    users = []  

    while True:
        # Gets user input in a loop
        name = input("Enter your name brah? ").strip()
        # Exit the loop if the user types 'exit'
        if name.lower() == "exit":  
            break

        # Will check if email is fit
        email = input("What's your email brah? ").strip()
        if not validate_email(email):  
            print("Invalid email format. Try again.")
            continue

        gym = input("What gym do you rep? or if you don't rep dont say anything ").strip()
        if gym:
            user = GymBro(name, email, gym)  
        else:
            user = User(name, email)  
        
        # Add the user to the list
        users.append(user) 
        # Shows confirmation
        print(f"Added {user.display_info()}.")  

    # Save all users to a file
    save_users_to_file(users)  
    print("All users saved to 'chestbrah_users.csv'.")

    print("Loading users from file:")
    # Load users from the file given
    loaded_users = load_users_from_file()  
    for user in loaded_users:
        print(user.display_info())  

# Testing
def test_validate_email():
    # Tests the email verification 
    # Valid email
    assert validate_email("zyzz@mirin.com") is True  
    
    # Invalid email
    assert validate_email("invalid-email") is False  
    assert validate_email("bro@chestbrah") is False  
    
    # Shows  results
    print("Email validation tests checked out brah")  

def test_file_io():
    # Tests saving and loading user data
    zyzz = User("Zyzz", "zyzz@mirin.com")
    chestbrah = User("Chestbrah", "chest@brah.com")
    test_users = [zyzz, chestbrah]
    # Save test users
    save_users_to_file(test_users, "test_users.csv")  # Save test users
    # Load test users
    loaded_users = load_users_from_file("test_users.csv")  # Load test users
    # Check that 2 users were loaded
    assert len(loaded_users) == 2  # Check that 2 users were loaded
    # Check first user's name
    assert loaded_users[0].name == "Zyzz"  
    # Check second user's email
    assert loaded_users[1].email == "chest@brah.com"  
    print("File I/O tests all checked out brah")  

if __name__ == "__main__":
    test_validate_email()
    test_file_io()
    main()

# I believe I used all from the sheet, I wanted to use the Zyzz topic for this project instead of the BMW one as I wanted to change it up. I had to refer back to lectures 9 and 11 because I had some troubles on line 75 as I tried to merge the oop and file io but got it in the end.
# also..... U mirin brah?
