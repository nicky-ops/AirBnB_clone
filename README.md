# 0x00. AirBnB clone - The console
The console is a command interpreter that is used to manage our full web application. 
In this project we will:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## Command interpreter a.k.a The console
The command interpreter will be used to manage objects of our project.
From the console, one should be able to:
* Create a new object(e.g New user or new place)
* Retrive an object from a file, a database e.t.c
* Do operations on objects(count, compute stats, ete..)
* Update attributes of an object.
* Destroy an object.
