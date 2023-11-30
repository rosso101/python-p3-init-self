#!/usr/bin/env python3

class Dog:
##This ensures that when you create an instance of the Dog class, you can pass a name and optionally a breed,
# with the breed defaulting to "Mutt" if not provided.
   def __init__(self, name, breed="Mutt"):
      self.name = name
      self.breed = breed
    
    fido = Dog("Fido")
    print(Fido.name)
    print(fido.breed)
   
   snoopy = Dog("Snoopy", "Beagle")
    print(snoopy.name)
    print(snoopy.breed) 