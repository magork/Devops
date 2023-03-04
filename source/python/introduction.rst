###############
0. Introduction
###############

Does it make sense to learn Python?

.. raw:: html

    <font color="blue">YES!</font>


More about on:
   
    - StackOverflow survey: https://insights.stackoverflow.com/survey
    - IEEE Spectrum: https://spectrum.ieee.org/top-programming-languages-2022

===============================
1. Is Python the best language?
===============================

**No**. There are no best languages.

Every language has pros and cons.

   - **Pro**: 
      - easy to learn
      - easy to code
      - has support from the community

   - **Con**: 
      - not fast or too performant
      - needs libraries on locally to run
      - management of libraries versions is weird

Why do **I** use Python and not another language?

Python is an **efficient language**: my applications will do more in fewer lines of code than many other languages would require. I can build cli applications, machine learning algorithms, and cloud microservices. And the community - I believe in **opensource** and its ability to deliver good alternatives.

==================
2. Python features
==================

* **Simple** - has a minimalist feel, the code feels like pseudo-code, allowing developers to concentrate on solving the problem not on writing the code. 
* **Easy to use** - most of the components are easy to pick up
* it's **FLOSS** - Free/Libre and Open Source Software
* **High-level** Language
* **Portable**
* **Interpreted**
* **Object-oriented** - everything in Python is an object
* **Extensive libraries** - from the web apps to ml - it does all

.. note::
   **Naming convention** - the Python programming language was named after the BBC program "Monty Python's Flying Circus" by Guido van Rossum.

==================
3. Python versions
==================

Release notes - what is new in every version?

https://docs.python.org/3.11/whatsnew/index.html

When to update?

- when new features are needed
   - bugs solved
   - performance improved
   - newly added API's
- when bored and you don't have work to do

==============
4. How to code
==============

**The Style Guide**
   A Python Enhancement Proposal is written when someone wants to alter the Python programming language (PEP).

   PEP 8, which teaches Python programmers how to style their code, is one of the first PEPs.

   Read more about the Python conventions at https://peps.python.org/pep-0008/


**Indentation**
   Per level of indentation, PEP 8 advises using four spaces.
   Four spaces allow for many levels of indentation on each line while also improving readability.
   People frequently indent text in word-processing documents using tabs rather than spaces.
   While this is effective for word-processing documents, the Python interpreter becomes confused when tabs and spaces are used together. 

**Line Length**
   The rule of thumb among Python programmers is that lines should be no more than 80 characters.
   Because most computers could only fit 79 characters on a single line in a terminal window, this rule originated in the past.
   Even if people can currently fit considerably longer lines on their devices, there are still good reasons to stick with the 79-character limit.
   Professional programmers frequently have multiple files open on the same screen, and by using the standard line length, they can see the whole line in two or three open files onscreen.
   Because some of the tools that automatically generate documentation for larger projects add formatting characters at the beginning of each comment line, PEP 8 also advises that you keep all of your comments to a maximum of 72 characters per line. 

**Blank Lines**
   Use blank lines to visually group the various components of your application.
   To arrange your files, utilize blank lines, but don't use them frequently. 

=================
The Zen of Python
=================

Experienced Python programmers will encourage you to avoid complexity and aim for simplicity whenever possible. The Python community's philosophy is contained in “The Zen of Python” by Tim Peters. You can access this brief set of principles for writing good Python code by entering import this into your interpreter.

.. code-block:: python

   python3.11

   # then run
   import this
