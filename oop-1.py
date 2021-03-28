import random


# Class (Blueprint)
class SoftwareEngineer:

    # Class attribute.
    software_engineer_skill = "keyboard magician"

    # Constructor __init__
    def __init__(self, position, name, age, level, salary, language):
        # Instance attributes.
        self.position = str(position).title().strip()
        self.name = str(name).title().strip() 
        self.age = str(age).title().strip()
        self.level = str(level).title().strip()
        self.salary = str(salary).title().strip()
        self.language = str(language).title().strip()
    
    # Instance methods

    # Displaying that the person is writing code.
    def programming(self):
        return f"{self.name} is writing code."

    # Showing information about the person in this class.
    def programmer_information(self):
        return f"Position: {self.position}, name: {self.name}, age: {self.age}, level: {self.level}, salary: {self.salary}."

    def programming_language(self):
        return "{} currently uses the programming language, {}.".format(self.name, self.language)
    
    # Dunder/magic method.
    def __str__(self):
        return f"Position = {self.position}, name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}."
    
    def __eq__(self, other):
        return "This statement is " + str(self.position == other.position).lower() + "."
    
    @staticmethod
    def entry(age):
        if age < 18:
            return "Invalid age for required job."
        
        elif age < 60:
            return "Valid age for required job."
        
        else:
            return "Sorry, but you are not qualified for this job."
    

# Instance (object) of SoftwareEngineer.
software_engineer1 = SoftwareEngineer("software engineer", "cory", 26, "Senior", "£90500", "python ")

# Using methods.
print(software_engineer1.programming())
print(software_engineer1.programming_language())
print(software_engineer1.programmer_information())
print("Details: ", end="")
print(software_engineer1.position, software_engineer1.name, software_engineer1.age, software_engineer1.level, software_engineer1.salary, sep=", ")

# Using class attribute outside of function.
software_skills = [SoftwareEngineer.software_engineer_skill, software_engineer1.software_engineer_skill]
print(software_engineer1.name, "is a", random.choice(software_skills).lower().strip(), end=".\n")
print(software_engineer1)

software_engineer2 = SoftwareEngineer("software engineer", " john", 34, "junior", "£74000", "python ")
print(software_engineer1 == software_engineer2) 

print(SoftwareEngineer.entry(60))