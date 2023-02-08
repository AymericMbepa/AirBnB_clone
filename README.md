0x00. AirBnB clone - The console
Write a command interpreter to manage your AirBnB objects.

This is the first step towards building our first full web application:
the AirBnB clone. This first step is very important because we will use what
you build during this project with all other following projects: HTML/CSS
templating, database storage, API, front-end integration…

Each task is linked and will help us to:

put in place a parent class (called BaseModel) to take care of the
initialization, serialization and deserialization of your future instances

* create a simple flow of serialization/deserialization:
Instance <-> Dictionary <-> JSON string <-> file

* create all classes used for AirBnB (User, State, City, Place…)
that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

Commang interpreter

* how to start
to start, we have to execute :
$ ./console.py

* how to use it
We can use it in two differents mode
- interractive mode
exemple:
$ ./console.py
(hbnb) help

Documented command (type help <topis>)
======================================
EOF help quit

(hbnb)
(hbnb)
(hbnb)
(hbnb) quit
$

- Noninterractive mode
Exemple:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$