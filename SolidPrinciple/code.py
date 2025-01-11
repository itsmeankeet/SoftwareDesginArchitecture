# 1. Single Responsibility Principle (SRP) - Each class should have only one responsibility
class Logger:
    def log(self, message):
        # Responsible only for logging messages
        print(f"Log: {message}")


class Calculator:
    def add(self, a, b):
        # Responsible only for adding numbers
        return a + b


class App:
    def run(self):
        # Responsible only for running the app
        pass


# 2. Open/Closed Principle (OCP) - Extend functionality without modifying existing code
class Shape:
    def area(self):
        # This method will be overridden in subclasses
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Circle-specific area calculation
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Rectangle-specific area calculation
        return self.width * self.height


# 3. Liskov Substitution Principle (LSP) - Subtypes should replace base types without breaking behavior
class Bird:
    def fly(self):
        # General flying behavior
        return "I can fly"


class Sparrow(Bird):
    def fly(self):
        # Specific flying behavior for sparrows
        return "Sparrow flies"


class Penguin(Bird):
    def fly(self):
        # Penguins don't fly, overriding the behavior
        return "Penguins can't fly"


# 4. Interface Segregation Principle (ISP) - Clients should not be forced to implement interfaces they don't use
class Printer:
    def print(self):
        # Responsible only for printing
        pass


class Scanner:
    def scan(self):
        # Responsible only for scanning
        pass


class MultiFunctionDevice(Printer, Scanner):
    def print(self):
        # Multi-function device can print
        pass

    def scan(self):
        # Multi-function device can scan
        pass


# 5. Dependency Inversion Principle (DIP) - High-level modules should not depend on low-level modules, but on abstractions
class NotificationService:
    def send(self, message):
        # Responsible for sending a notification
        pass


class EmailService(NotificationService):
    def send(self, message):
        # Responsible for sending email notifications
        print(f"Sending Email: {message}")


class SMSService(NotificationService):
    def send(self, message):
        # Responsible for sending SMS notifications
        print(f"Sending SMS: {message}")


class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        # High-level module that depends on abstraction (NotificationService)
        self.service.send(message)


# Example Usage of the Classes
if __name__ == "__main__":
    # SRP Example
    logger = Logger()
    calc = Calculator()
    result = calc.add(5, 3)
    logger.log(f"Result is {result}")

    # OCP Example
    shapes = [Circle(5), Rectangle(4, 6)]
    areas = [shape.area() for shape in shapes]
    print(areas)

    # LSP Example
    def make_bird_fly(bird: Bird):
        print(bird.fly())
    
    make_bird_fly(Sparrow())   # Output: Sparrow flies
    make_bird_fly(Penguin())   # Output: Penguins can't fly

    # ISP Example
    mfd = MultiFunctionDevice()
    mfd.print()  # Output: Printing functionality
    mfd.scan()   # Output: Scanning functionality

    # DIP Example
    email_service = EmailService()
    sms_service = SMSService()

    email_manager = NotificationManager(email_service)
    email_manager.notify("Hello via Email!")  # Output: Sending Email: Hello via Email!

    sms_manager = NotificationManager(sms_service)
    sms_manager.notify("Hello via SMS!")  # Output: Sending SMS: Hello via SMS!
