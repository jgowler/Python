# Practicing Classes and Class inhertience

These two files were created to briefly go over how kto create Classes and Child Classes in Python. Shared attributes will be created in the Parent Class and Inherited by the Child Class. Unique attirbutes and Methods of Child Classes will be added to each where necessary.

## def __init__()

- "__init__" is a special method in Python classes, called the constructor.
- Its main job is to initialize the object’s attributes with the values you provide.

## super()
- "super()" is a built-in Python function that lets you call methods from a parent (or superclass) inside a child (or subclass).
- It’s commonly used in class inheritance to extend or reuse the behavior of the parent class.
- Most often, you use it to call the parent’s **__init__** method so the parent class can initialize its attributes properly.
- Used to avoid rewriting code that’s already in the parent class.

## Class Methods

### What is a method in a class?
- Methods are functions that are defined _inside_ a class.
Example:
    `def weapon_attack(self):
        if self.weapon == True:
            damage = self.str * 2
            print(f"{self.name} used their weapon to attack for {damage} damage!")
            print(f"{self.name}'s weapon broke from the attack.")
            self.weapon == False
        else:
            print(f"{self.name} does not have a weapon, the attack failed.")`

- They describe the behaviors or actions that instances (objects) of the class can perform.
- When called, methods have access to the instance that called them via the special parameter self.
- Methods can access or modify the instance’s attributes (as seen in the above example the _self.weapon_ keyword argument is changed from _True_ to _False_ after use.)