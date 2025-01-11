# High Cohesion Example
class UserAccount:
    def __init__(self):
        self.username = ""
        self.password = ""

    def register_user(self, username, password):
        self.username = username
        self.password = password
        print(f"User {username} registered.")

    def login_user(self, username, password):
        print("Login successful" if self.username == username and self.password == password else "Login failed.")

# Low Cohesion Example
class Utility:
    def print_invoice(self):
        print("Printing invoice...")

    def send_email(self, email):
        print(f"Sending email to {email}...")

# High Coupling Example
class Database:
    def save_data(self, data):
        print(f"Saving {data} to the database.")

class UserAccountHighCoupling:
    def __init__(self, database):
        self.database = database

    def save_user(self, user):
        self.database.save_data(user)
        print(f"User {user} saved.")

# Low Coupling Example
class DatabaseInterface:
    def save_data(self, data):
        raise NotImplementedError

class FileDatabase(DatabaseInterface):
    def save_data(self, data):
        print(f"Saving {data} to a file.")

class UserAccountLowCoupling:
    def __init__(self, database):
        self.database = database

    def save_user(self, user):
        self.database.save_data(user)
        print(f"User {user} saved.")
