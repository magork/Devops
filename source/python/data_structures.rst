#################################
2. Variables and Data structures
#################################

Variables 
----------

Variables Are Labels - Variables are often described as boxes you can store values in - a variable references a certain value.

When declaring a variable we use the syntax: `name = value`

.. code-block:: python

   x = 1

We can also do multiple assignments

.. code-block:: python

   x, y, z = "A", "B", "C"

   print(x, y, z)

Naming
-------

When you are using variables in Python, you need to adhere to a few rules and guidelines. Breaking some of these rules will cause errors; other guidelines just help you write code that is easier to read and understand. Be sure to keep the following variable rules in mind:

   - Variable names can contain only **letters**, **numbers**, and **underscores**.
   - Variable names are **case-sensitive** (``name``, ``Name`` and ``NAME`` are three different variables)
   - They can start with a **letter or an underscore**, but not with a number. For instance, you can call a variable ``name_1`` but not ``1_name``.
   - **Spaces are not allowed** in variable names, but underscores can be used to separate words in variable names. For example, ``first_name`` works, but ``first name`` will cause errors.
   - **Avoid using Python keywords** and function names as variable names; that is, do not use words that Python has reserved for a particular programmatic purpose, such as the word print. Read more:  https://docs.python.org/3/reference/lexical_analysis.html#keywords
   - Variable names should be **short but descriptive**. For example, ``name`` is better than ``n``, ``first_name`` is better than ``f_n``, and ``name_length`` is better than ``length_of_persons_name``.
   - Be careful when using the lowercase letter ``l`` and the uppercase letter ``O`` because they could be confused with the numbers ``1 and 0``.

Naming conventions 
+++++++++++++++++++

In **Python** naming conventions will not affect your code, but will affect your way for working in the team (in other languages naming convention matters)

We have 4 different ways of declaring:

1. **Snake case** (ex: some_variable) 
2. **Screaming Snake case** (ex: SOME_VARIABLE)
3. **Pascal case** (ex: SomeVariable)
4. **Camel case** (ex: someVariable)

Read more about the Python conventions in https://peps.python.org/pep-0008/

**I** use them like this:

- **Snake case** - for functions, methods, attributes, variables (this is the preferred way in Python)

Function names should be lowercase, with words separated by underscores as necessary to improve readability.

Is prefered ``def function_name():`` not ``def functionName():``.

.. code-block:: python
   
   first_name = input("Enter your name: ")

- **Screaming Snake case** - Constants  

.. code-block:: python
   
   PI = 3.14

- **Pascal case** - defining class name.

.. code-block:: python
   
   class Student:
      def __init__(self, name, age): 
         self.name = name
         self.age = age

      def displayInfo(self): # class method
         print('Student Name: ', self.name,', Age: ', self.age)

- **Camel case**- to name some methods (ex: toJson, fromFile, updateFile) - because when you are using them they look like this ``Student.displayInfo``

Data types
-----------

In Python3.6, PEP 498 introduces a new kind of string literals: f-strings, or formatted string literals.

Read more about f-strings https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498

1. Strings
-----------

In Python, strings are enclosed in either single or double quotation marks. Single quotes will not let variable pass, so be careful.

.. code-block:: python
   
   single_name = 'skillab'
   doubleName = "skillab"

   print("Course name is " + single_name)
   # or
   print(f"Course name is {single_name}")

String Manipulation
++++++++++++++++++++

.. code-block:: python
   
   print("skillab".title())

   name = "skillab"

   print(name.title())
   print(name.lower())
   print(name.upper())
   print(name.replace('a','A'))

   # How to find out all the available alternatives
   dir(name)


Magic methods
++++++++++++++ 

``__len__()``

One of the many magic methods in the Python programming language, ``__len__`` is primarily used to implement the ``len()`` function because every time the ``len()`` function is called, the magic method ``__len__`` is also called internally.

After all is said and done, it returns an integer value larger than or equal to zero, which is the length of the object for which it was called. 

.. code-block:: python
   
   print("skillab".__len__())
   print(len("skillab"))

2. Numbers
-----------

Python supports two types of numbers:

 - integers(whole numbers)
 - floating point numbers(decimals).

.. code-block:: python
    
   # When declaring a variable we use the syntax
   # name = value
   x = 1
   xint = int(x)
   xfloat = float(x)
   universe_age = 14_000_000_000

   print(x)
   print(xint)
   print(xfloat)
   print(universe_age)

   print(type(x))
   print(type(xint))
   print(type(xfloat))

   print(dir(x))
   print(dir(xint))
   print(dir(xfloat))

Number operations
++++++++++++++++++++

.. code-block:: python

   # add 
   print(1+2)
   # subtract
   print(1-2)
   # multiply
   print(1*2)
   # divide
   print(1/2)
   # modulo
   print(1%2)

3. Lists
---------

A list is a collection of objects in a specific sequence.
A list can contain anything you want, and there is no requirement that the items on it link to one another in any specific way.
It's a good idea to name your list in the plural, such as letters, numerals, or names, because lists typically contain many elements.

.. code-block:: python

   animals = ["cat", "dog", "python"]

   print(animals)

   # Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.
   print(animals[2])

   # You can also format the result
   print(animals[2].title())

List Manipulation
++++++++++++++++++

The majority of lists you create will be dynamic, meaning that when your program executes, you'll add, update and remove items from the list you've created. 

.. code-block:: python

   # Add elements
   animals.append("monkey")
   print(animals)

   # Insert element at any position
   animals.insert(0, "rabbit")
   print(animals)

   # Remove elements by position
   del animals[3]
   print(animals)

   # Removing an Item Using the pop() Method
   # Example want to remove a user from a list of active members and then add that user to a list of inactive members.
   # pop() with no argument last element
   # pop(1) 2nd element
   popped_animal = animals.pop()

   # Remove elements by value
   animals.remove("python")

.. warning:: 

   Only the first instance of the value you specify is removed by the ``remove()`` method.
   You'll need to use a loop if there's a chance that the value could appear more than once in the list to ensure that all instances are eliminated.

.. code-block:: python

   digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
   min(digits)
   max(digits)
   sum(digits)

List Organization
++++++++++++++++++

Because you can't always control the order in which your users submit their data, your lists will frequently be generated in an unpredictable order.

.. code-block:: python

   animals = ['rabbit', 'cat', 'dog', 'python', 'monkey']
   # how long is the list
   len(animals)
   
   print(animals)

   animals.sort()
   animals.sort(reverse=True)

   # sort() is a irreversible procedure
   # if you need something temporary without affecting the original list use sorted(list_name)
   print("Here is the original list:")
   print(animals)

   print("\nHere is the sorted list:")
   print(sorted(animals))

   print("\nHere is the original list again:")
   print(animals)

.. warning::

   When all the values are not lowercase, sorting a list alphabetically becomes a little more challenging.
   When determining a sort order, capital letters can be interpreted in a variety of ways, and specifying the precise order can be more difficult than we want to handle right now.

Avoiding Index Errors When Working with Lists
+++++++++++++++++++++++++++++++++++++++++++++++

When you are working with lists for the first time, one type of error is frequent to see is Index error.

.. code-block:: python

   animals = ['rabbit', 'cat', 'dog', 'python', 'monkey']

   print(animals[5])

   # Instead of using last element by explicitly using position value we can use
   print(animals[-1])

4. Dictionaries
-----------------

In Python, a dictionary is a collection of key-value pairs.
Each key has a value associated with it, and you may use a key to get that value.
The value of a key could be an integer, string, list, dictionary, or even another dictionary.
In actuality, you may use any Python-created object as a value in a dictionary.

.. code-block:: python

   animals = { 'reptile': 'python', 'primates': 'monkey', 'mammal': 'dog'}
   
   # Accessing elements using key
   animals['primates']

   # Accessing keys
   animals.keys()

   # Accessing values
   animals.values() 

   # Loop through dictionary values
   for animal in animals.values():
      print(animal.title())

   muscle_cars = {
   "brand": "Dodge",
   "model": "Challenger",
   "year": 1970
   }

   # Add new elements in dictionary
   muscle_cars["color"] = "black"

   # Update dictionary
   muscle_cars.update({"color": "red"})

   # Remove items
   # `pop()` method removes the item with the specified key name
   muscle_cars.pop("color")

   # `popitem()` method removes the last inserted item
   muscle_cars.pop("year")

   # `del` keyword removes the item with the specified key name
   del muscle_cars["model"]

   # clear() method empties the dictionary
   muscle_cars.clear()