###########
6. Classes
###########

Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code. The data is in the form of fields (often known as attributes or properties), and the code is in the form of procedures (often known as methods).

Generating an object from a class is called instantiation.
You work with instances of a class, which are created by the process of instantiating an object from a class. 
Using functions 
----------------

.. code-block:: python
    
    class Student:
        """
        A class is used to represent a student.

        ...

        Attributes
        ----------
        name: str
            the name of the students
        age: int
            the age of the students

        Methods
        -------
        learn()
            Simulate a student's learning.
        take_exam()
            Simulate taking over good results.
        """

        def __init__(self, name, age):
            """Initialize name and age attributes.
            
            Attributes
            ----------
            name: str
                the name of the students
            age: int
                the age of the students
            
            Returns:
                None
            """
            self.name = name
            self.age = age

        def learn(self):
            """Simulate a student's learning.

            Prints status

            Attributes
            ----------
            name: str
                the name of the students
            age: int
                the age of the students
            
            Returns:
                None
            """
            print(f"{self.name} is now learning.")

        def take_exam(self):
            """Simulate taking over good results.
            
            Prints encouragement 

            Attributes
            ----------
            name: str
                the name of the students
            age: int
                the age of the students
            
            Returns:
                None
            """
            print(f"{self.name} did great!")

    print(f"Student1 is {student1.name} and is {student1.age}")
    print(f"Student2 is {student2.name} and is {student2.age}")

    student1 = Student("John Wick", 47)
    student2 = Student("Macaulay Culkin", 12)

A method is a function that is a part of a class.
Everything you learned about functions also applies to methods; the only difference in practice is that we'll refer to methods as methods. 