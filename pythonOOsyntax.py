""" Week 3 - Object-Oriented Paradigm in Python """

# Example 1
class Car:
    def __init__(self, x, y):
        self.color = x
        self.maker = y

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

myCar = Car("white","Hyundai")
print(myCar)
myCar.start_engine()
myCar.stop_engine()
print(myCar.color)

# Example 2
class FIUStudent():
    minimum_grade = 93

    def __init__(self, firstName, lastName, pid, email, grade):
        self.firstName = firstName
        self.lastName = lastName
        self.pid = pid
        self.email = email
        self.grade = grade

    def current_grade(self):
        return f"{self.firstName.title()} {self.lastName.title()}\'s current grade is {self.grade}."

student1 = FIUStudent("greg","reis",1234,"gmuradre@fiu.edu",86)
print(student1.current_grade())
student2 = FIUStudent("alfredo","bayuelo",2345,"abayuelo@fiu.edu",95)
print(student2.current_grade())
print(student1.minimum_grade,student2.minimum_grade)
student2.minimum_grade = 96
print(student1.minimum_grade,student2.minimum_grade)
FIUStudent.minimum_grade = 89
print(student1.minimum_grade,student2.minimum_grade)

# Example 3

class Robot():
    def __init__(self, name, weight,battery_life,price):
        self.name = name
        self.weight = weight
        self.battery_life = battery_life
        self.price = price

    def introduce(self):
        return (f"I'm {self.name.title()} and my"
                f" battery last {self.battery_life} hours.")

robot1 = Robot("zig",50,4,399.99)
print(robot1.introduce())

class AquaticRobot(Robot):
    def __init__(self, name, weight,battery_life,price, sensors, motors, isAutonomous):
        super().__init__(name, weight,battery_life,price)
        self.sensors = sensors
        self.motors = motors
        self.isAutonomous = isAutonomous

    def environment(self,water):
        return (f"I'm {self.name.title()} and I am an aquatic robot that operates in"
                f" {water} water.")

robot2 = AquaticRobot("Eco",170,8,140000,["temp","pH"],3,True)
print(robot2.environment("fresh"))
print(robot2.introduce())

# Example 4

from abc import abstractmethod, ABC

class StreamingService(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def add_subscriber(self, username):
        pass

    @abstractmethod
    def remove_subscriber(self, username):
        pass

    @abstractmethod
    def display(self):
        pass

class VideoStreamingService(StreamingService):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.subscribersList = []

    def play(self):
        print("I am a rich streaming service and production company.")

    def add_subscriber(self, username):
        self.subscribersList.append(username)

    def remove_subscriber(self, username):
        try:
            self.subscribersList.remove(username)
        except ValueError:
            pass
    def display(self):
        print("I provide tv shows and movies to my subscribers.")

netflix = VideoStreamingService("Netflix",15.99)
netflix.add_subscriber("greg")
print(netflix.subscribersList)