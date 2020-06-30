![AirBnB_clone](/images/AirBnB.png?raw=true "Title")

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

![AirBnB_clone](/images/AirBnB_clone.png?raw=true "Title")

### classes:
- `BaseModel`: parent class to take care of the initialization and serialization of future instances.
- `City`, `Place`, `Review`, `State`, `User`, `Amenity`: objects used for AirBnB, they inherit from `BaseModel`.
- `FileStorage`: storage engine to save objects, serialization and deserialization.
- `HBNBCommand`: The console to manage the AirBnB objects (this console was made with the module 'cmd').


### How to start the console:
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
```


### How to use the console:

- `quit` and `EOF` to exit the program.
	```
	$ ./console.py
	(hbnb)
	(hbnb)
	(hbnb) quit
	$
	```

- `create`: Creates a new instance of a class (`User`, `Place`, `State`, `City`, `Amenity`, `Review`), saves it (to the JSON file) and prints the id.
	```
	(hbnb) create User
	49faff9a-6318-451f-87b6-910505c55907
	```

- `show`: Prints the string representation of an instance based on the class name and id.
	```
	(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
	[User] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
	```

- `destroy`: Deletes an instance based on the class name and id (save the change into the JSON file). `Ex: $ destroy BaseModel 1234-1234-1234.`
	```
	(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
	(hbnb)
	```

- `all`: Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` or `$ all`.
	```
	(hbnb) all
	["[Place] (af54dd4c-4079-4aed-bbe9-48f41eb454ec) {'updated_at': datetime.datetime(2020, 6, 29, 15, 22, 9, 889041), 'id': 'af54dd4c-4079-4aed-bbe9-48f41eb454ec', 'created_at': datetime.datetime(2020, 6, 29, 15, 22, 9, 889026)}", "[User] (af517061-350a-4f2c-8ba0-1a4165a7e567) {'updated_at': datetime.datetime(2020, 6, 29, 15, 22, 6, 98064), 'id': 'af517061-350a-4f2c-8ba0-1a4165a7e567', 'created_at': datetime.datetime(2020, 6, 29, 15, 22, 6, 98056)}", "[City] (f2d09f45-7af7-4db2-abab-23a350fad13c) {'updated_at': datetime.datetime(2020, 6, 29, 15, 22, 15, 969404), 'id': 'f2d09f45-7af7-4db2-abab-23a350fad13c', 'created_at': datetime.datetime(2020, 6, 29, 15, 22, 15, 969390)}"]
	(hbnb)
	(hbnb) all Place
	["[Place] (af54dd4c-4079-4aed-bbe9-48f41eb454ec) {'updated_at': datetime.datetime(2020, 6, 29, 15, 22, 9, 889041), 'id': 'af54dd4c-4079-4aed-bbe9-48f41eb454ec', 'created_at': datetime.datetime(2020, 6, 29, 15, 22, 9, 889026)}"]
	```

- `update`: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
	- Usage: `update <class name> <id> <attribute name> "<attribute value>"`
	- Only one attribute can be updated at the time.
	- A string argument with a space must be between double quote.

	```
	(hbnb) show User f7f99708-e395-463a-b035-09a731ef8302
	[User] (f7f99708-e395-463a-b035-09a731ef8302) {'updated_at': datetime.datetime(2020, 6, 29, 15, 27, 48, 421148), 'id': 'f7f99708-e395-463a-b035-09a731ef8302', 'created_at': datetime.datetime(2020, 6, 29, 15, 27, 48, 421135)}
	(hbnb)
	(hbnb) update User f7f99708-e395-463a-b035-09a731ef8302 name "Diana Caro"
	(hbnb)
	(hbnb) show User f7f99708-e395-463a-b035-09a731ef8302
	[User] (f7f99708-e395-463a-b035-09a731ef8302) {'id': 'f7f99708-e395-463a-b035-09a731ef8302', 'created_at': datetime.datetime(2020, 6, 29, 15, 27, 48, 421135), 'updated_at': datetime.datetime(2020, 6, 29, 15, 27, 48, 421148), 'name': 'Diana Caro'}
	(hbnb)
	```

- `help`: to get information about the commands.
	```
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  all  count  create  destroy  help  quit  show  update

	(hbnb) help quit
	Quit command to exit the program

	(hbnb)
	```

### Using the console by class name:

- `<class name>.all()`: to retrieve all instances of a class.
- `<class name>.count()`: to retrieve the number of instances of a class.
- `<class name>.show(<id>)`: to retrieve an instance based on its ID.
- `<class name>.destroy(<id>)`: to destroy an instance based on his ID.
- `<class name>.update(<id>, <attribute name>, <attribute value>)`: to update an instance based on his ID.
- `<class name>.update(<id>, <dictionary representation>)`: to update an instance based on his ID with a dictionary.

### Run unittests
`python3 -m unittest discover tests`

### Diagram of the program

![diagram](/images/program_diagram.jpg?raw=true "Title")

When the console is started, it imports `storage`, which is an instance of the storage engine (`class FileStorage`). The file in change to create this instance is `/models/__init__.py`, whish also call the method `reload()` of `storage` just after the creation of this instance.

`reload()` deserialize the `file.json` file, which contains all the JSON string representation of the AirBnB objects (`User`, `City`, `Place`, `Review`, `Amenity`, `State`) and add all those objects to the dictionary `objects` (which is a class attribute of `class FileStorage`).

### Example of command create
![diagram](/images/command_create.jpg?raw=true "Title")
