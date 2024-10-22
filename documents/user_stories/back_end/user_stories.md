# User Stories Back End

---

# User Story #1

## Create an API (Application Programmer Interface)

- As a front-end developer
- Want to be able to access the back-end of the system through an API
- For access to data program

## SAMPLE TASKS FOR REFERENCE

### TASK a) Create a minimal API that can answer answer a dummy request

ASSIGNEE: Esteban (JE-CM)

### TASK b) Improve the API with the various operations required by the program

DESCRIPTION: TBD
ASSIGNEE: TBD

---

# User Story #2

## Add API Access Control

- As an admin
- Want to be able to control who can access the API
- For limiting improper usage (prevent spam to API) and ensuring that source IP is as expected

---

# User Story #3

## User Data Access as Administrator

- As an adminitrator
- Want to be able to do CRUD (Create, Read, Update, Delete) operations on all user data for all users
- For user administration needs

---

# User Story #4

# Facility Data Access as Administrator

- As an adminitrator
- Want to be able to do CRUD operations on all facility data, which is not accessible to any users
- For facility administration needs

---

# User Story #5

## User Data Access as Client

- As a client
- Want to be able to do CRUD operations on all user data for the current user
- For personal user needs

---

# User Story #6

## Facility Data Access as guest/client

- As a guest/client
- Want to be able to do Read/search/etc operations on all facility data
- For personal/prospective user needs

---

# User Story #7

## Developer Documentation

- As a developer of this project
- I want to be able to document all project design decisions, best practices, work tracking, etc
- For making it easier to understand the project and remember important details later

ASSIGNEE: matthew-silva
ASSIGNEE: JE-CM

NOTE: This story will probably stay open for some weeks as we document the design of the project, and then close once we start documenting the individual subsystems of the project (we will create tickets for each subsystem or complete the documentation during the subsystem implementation tickets).

---

# User Story #8

## Create a skeleton for the backend

- As a developer
- I want a basic piece of python code that I can extend with all other functionality
- For making it easy to start working on the backend

ASSIGNEE: matthew-silva

---

# User Story #9

## Authentication System

- As a user
- I want to have my passwords securely stored and checked when entering them
- For data security reasons

Assignee: matthew-silva

---

# User Story #10

## Create Basic comunication with Database

- As a developer
- I want a basic database of some kind which can store system and user data
- For the basic operation of the program, such as providing user login, user data display, system data display

ASSIGNEE: matthew-silva

---

# USER STORY #19

- As a developer
- I want to to have user stories defined which follow the design of "Phase 1" of the product design document provided by Geraldine (ggm.100423@gmail.com), the project UI/UX designer.
- So that my development efforts are well-guided for creating a proper user experience that supports the product vision.

ASSIGNEE: matthew-silva

---

# USER STORY 20

## Support user-side database operations of self-storage unit modality

- As a front-end developer
- I want an OrganizedStorageDatabase object which supports the user-side of the self-storage units modality of the Organized Storage project. The user operations of the self-storage modality require basic customer data as well as a reference to the storage unit(s) being used by the customer and the price the customer pays for those units.
- So that I can easily access this info for front-end development without knowing anything about the database

# USER STORY 21

## Support unit-side database operations of self-storage unit modality

- As a front-end developer
- I want an OrganizedStorageDatabase object which supports the unit-side of the self-storage units modality of the Organized Storage project. The unit-side operations of the self-storage modality require a unit ID, list of authorized user IDs, location, size, status of temperature regulation, status of vehicular access for each unit.
- NOTE: Potentially make this class have an instances of OrganizedStorageDatabase instead of inheriting from OrganizedStorageDatabase so that this class can have add_unit instead of add_user method
- So that I can easily access this info for front-end development without knowing anything about the database

# USER STORY 22

## Support user-side database operations of communal storage unit modality

- As a front-end developer
- I want an adapted OrganizedStorageDatabase object which supports the user-side operations of the communal storage units modality of the Organized Storage project. The user operations of the communal-storage modality require basic customer data as well as a list of the items being stored by the customer (item ID).
- So that I can easily access this info for front-end development without knowing anything about the database

# USER STORY 23

## Support item-side database operations of communal storage unit modality

- As a front-end developer
- I want an adapted OrganizedStorageDatabase object which supports the item-side operations of the communal storage units modality of the Organized Storage project. The item operations of the self-storage modality require an item ID, list of authorized user IDs, basic description, optional longer description, one or more photographs, and a size category for each item.
- NOTE: Potentially make this class have an instances of OrganizedStorageDatabase instead of inheriting from OrganizedStorageDatabase so that this class can have add_item instead of add_user method
- So that I can easily access this info for front-end development without knowing anything about the database

# USER STORY 24

## Create OrganizedStorage class for central organization of all backend objects

- As a front-end developer
- I want a simplified OrganizedStorage object which will contain all of the objects necessary for the Organized Storage backend, such as all the databases. This object should have functions for common business operations like:
  - add user to self-storage
  - Add user to authorized list for self-storage unit
  - add self-storage unit
  - Check for if user is authorized to access self-storage unit
  - Notify authorized users on access to self-storage unit
  - Show all authorized users on unit
  - Show all units which can be accessed by user
  - Show unit charactertics (size, temperature controlled, vehicular access)
  - add user to communal-storage
  - Add user to authorized list for communal-storage item
  - Add communal-storage item
  - Check for if user is authorized to pickup communal-storage item
  - Show list of items owned by user
  - Show video feed of communal area (TODO)
- To simplify development and create a place for pure business logic

ASSIGNEE: matthew-silva

# USER STORY 25

## Convert the result of the user_search function to a dictionary with the column names as the keys

- As a developer
- It would be convenient to have the user_search function return a dictionary rather than a list of columns
- For making it easier to interpret and process the results
- NOTE: Let's keep the original functionality available and toggle with a parameter called return_dict=True

ASSIGNEE: matthew-silva

# USER STORY 26

## Clean up OrganizedStorageDatabase function return values

- As a developer
- I want the OrganizedStorageDatabase functions, such as add_user, user_search, and remove_user to have useful and consistent return values
- To increase their utility during development
- NOTE: Clean up the return values for each OrganizedStorageDatabase function by having the execute_query function return a dictionary of every possible return value from the cursor, which consuming functions can use as they need. Currently our execute_query function only returns very limited info.

ASSIGNEE: matthew-silva

# USER STORY 27

## Add corner cases to OrganizedStorageDatabase testing

- As a developer
- I want the OrganizedStorageDatabase to behave appropriately in common corner cases like trying to remove a user that does not exist (throw exception), trying to update a user that does not exist (throw exception), trying to search a user that does not exist (return nothing), etc.
- For giving the class more stability which will make it suitable for indirect consumption by the frontend

ASSIGNEE: JE-CM

# USER STORY 28

## Add unit tests for db.py compatible with unittest module

- As a developer
- I want to have consistent and easy to use unit tests in the db.py file similar to what we already have for the OrganizedStorageDatabase_unittest.py
- For increasing test coverage and consistency
