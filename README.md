# AirBnB clone - The console

'The console' is a command interpreter to manage the AirBnB objects:

- Create a new object (ex: a new User or a new Place).
- Save objects to a file (JSON format).
- Retrieve objects from a file (JSON format).
- Update attributes of an object.
- Destroy an object.

With this console we have a simple flow of serialization/deserialization:
Instance <-> Dictionary <-> JSON string <-> file.

This is the first step towards building a full web application: the AirBnB clone. This will be used with all other following projects: HTML/CSS templating, database storage, API, front-end integration, etc.

--- imagen ---


#### classes:
- `BaseModel`: parent class to take care of the initialization and serialization of future instances.
- `City`, `Place`, `Review`, `State`, `User`, `Amenity`: objects used for AirBnB, they inherit from `BaseModel`.
- `FileStorage`: storage engine to save objects, serialization and deserialization.
- `HBNBCommand`: The console to manage the AirBnB objects (this console was made with the module 'cmd').


#### How to start the console:
```
$ ./console.py
```

It should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
$

```

And in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
```


#### How to use the console:

#### commands:
- `quit` and `EOF` to exit the program.

```
vagrant@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$
```

- `create`: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: `$ create BaseModel`.

- `show`: Prints the string representation of an instance based on the class name and id. Ex: `$ show BaseModel 1234-1234-1234`.
- `destroy`: Deletes an instance based on the class name and id (save the change into the JSON file). `Ex: $ destroy BaseModel 1234-1234-1234.`

- `all`: Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` or `$ all`.

- `update`: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`.
	- Usage: `update <class name> <id> <attribute name> "<attribute value>"`
Only one attribute can be updated at the time.
A string argument with a space must be between double quote.




- `help`: to get information about the commands.







- create all unittests to validate all our classes and storage engine.