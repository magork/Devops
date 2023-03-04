#!/usr/bin/env python3.11

animals = ['rabbit', 'cat', 'dog', 'python', 'monkey']

if 'python' in animals:
    animals.remove('python')
    print(animals)
        
if "whale" not in animals:
    animals.append("whale")
    print(animals)

animals = []
if not animals:
    animals.append("python")
    print(animals)
else:
    print(animals)