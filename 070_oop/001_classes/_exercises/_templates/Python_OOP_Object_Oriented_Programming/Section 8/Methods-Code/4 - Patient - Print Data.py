class Patient:

    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def display_data(self):
        print(f"Name: {self.name}; Age: {self.age}; Diagnosis: {self.diagnosis}")

# Create the instance
patient1 = Patient("Daniel", 56, "Femur Fracture")

# Call the method
patient1.display_data()
