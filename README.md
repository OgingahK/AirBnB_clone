**An AirBnB Console**


**Description**

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

**The Console**

. Create your data model
. Manage (create, destroy, update) via a console/ command interpreter
. Store and persist objects to a file(JSON) file

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

**Commands Available:**

. show
. create
. update
. destroy
. count

**Command Interpreter**

It is coupled with the backend and file storage system, it can perfom the following actions:

. Create a new object (ex: a new User or a new Place)
. Retrieve an object from a file, a database etc…
. Do operations on objects (count, compute stats, etc…)
. Update attributes of an object
. Destroy an object

**How to use it:**

Our console will work like this in the interactive mode:

`
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
`

In order to use the console in intaractive mode, run the file `console.py` by itself:

`$ ./console.py`

While running in interactive mode, the displayed prompt for input:

`$ ./console.py
(hbnb) `

To quit the console, enter the command `quit`, or input the EOF signal (`ctrl+D`):

`$ ./console.py
(hbnb) quit
$`

`$ ./console.py
(hbnb) EOF
$`

But also like this in non-interactive mode:

`
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
`


**How to test**

Run all test:

`$ python3 unittest -m discover tests`

Run a specific single test:

`$ python3 unittest -m tests/test_console.py`
