class Pet:
    def __init__(self):
        self.name = ""
        self.animal_type = ""
        self.age = 0

    def set_name(self, name):
        self.name = name

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def get_age(self):
        return self.age


def main():
    # Create a Pet object
    pet = Pet()

    # Prompt the user to enter pet details
    name = input("Enter pet's name: ")
    animal_type = input("Enter pet's animal type: ")
    age = int(input("Enter pet's age: "))

    # Set pet's attributes using the setter methods
    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    # Display pet's details using accessor methods
    print("\nHere are your Pet's Details:")
    print("Pet Name:", pet.get_name())
    print("Animal Type:", pet.get_animal_type())
    print("Pet Age:", pet.get_age())


if __name__ == "__main__":
    main()

