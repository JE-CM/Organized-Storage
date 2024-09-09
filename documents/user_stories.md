# User Stories

# User Story #1

## Create an API (Application Programmer Interface)

- As a front-end developer
- Want to be able to access the back-end of the system through an API
- For access to data program

## SAMPLE TASKS FOR REFERENCE

### TASK a) Create a minimal API that can answer answer a dummy request
ASSIGNEE: Esteban 

### TASK b) Improve the API with the various operations required by the program
DESCRIPTION: TBD
ASSIGNEE:  TBD


# User Story #2

## Add API Access Control

- As an admin
- Want to be able to control who can access the API
- For limiting improper usage (prevent spam to API) and ensuring that source IP is as expected

# User Story #3

## Simple command-line UI

- As an early program tester/developer
- Want to be able to use a command-line interface to access the program's API
- For early testing of the program

# User Story #4

## User Data Access as Administrator

- As an adminitrator
- Want to be able to do CRUD (Create, Read, Update, Delete) operations on all user data for all users
- For user administration needs

# User Story #5

# Facility Data Access as Administrator

- As an adminitrator
- Want to be able to do CRUD operations on all facility data, which is not accessible to any users
- For facility administration needs

# User Story #6

## User Data Access as Client

- As a client
- Want to be able to do CRUD operations on all user data for the current user
- For personal user needs

# User Story #6

## Facility Data Access as guest/client

- As a guest/client
- Want to be able to do Read/search/etc operations on all facility data
- For personal/prospective user needs

# User Story #7

## Developer Documentation

- As a developer of this project
- I want to be able to document all project design decisions, best practices, work tracking, etc
- For making it easier to understand the project and remember important details later

ASSIGNEE: matthew-silva
ASSIGNEE: JE-CM

NOTE: This story will probably stay open for some weeks as we document the design of the project, and then close once we start documenting the individual subsystems of the project (we will create tickets for each subsystem or complete the documentation during the subsystem implementation tickets).

# User Story #8

## UI/UX Designer Integration

- As a UI developer of this project
- I want to receive and follow the specification of some UI/UX design provided by the UI/UX designer of the project, Geraldine (ggm.100423@gmail.com). I assume this UI/UX design will be some sort of figma wireframe or something similar but the specifics are left to the designer, them being the expert in this area.
- For making our UI implementation process much easier (existing design makes it so much easier) and reducing the amount of refinement and rework (starting with a UI/UX designer's full design is much better than starting with a programmer's vague idea)

# User Story #9

## Web Interface Implementation Integration

- As a UI developer of this project
- I want to create a web interface front-end for the project using the UI/UX designer's design as a plan. I want to use html/css/javascript to create the actual UI.
- For improving the user experience compared to the minimal command-line interface which already exists

# User Story #10

## UI/UX Design Creation

- As a UI/UX designer of this project
- I want to create a UI/UX design for this project. I will need a source of specifications for the services the project is supposed to provide. 
- For creating a clear plan for the UI implementation team

# User Story #11

## Create a skeleton for the backend

- As a developer
- I want a basic piece of python code that I can extend with all other functionality
- For making it easy to start working on the backend

ASSIGNEE: matthew-silva

# User Story #12

## Authentication System

- As a user
- I want to have my passwords securely stored and checked when entering them
- For data security reasons

Assignee: matthew-silva

# User Story #13

## Create Basic Database

- As a developer
- I want a basic database of some kind which can store system and user data
- For the basic operation of the program, such as providing user login, user data display, system data display

ASSIGNEE: matthew-silva

# User Story #14

## Create Database Functions Specific to Organized Storage User Management

- As a backend developer
- I need user add / delete / edit functions to be able to easily interface with the database without knowing anything about SQL
- For doing backend work without SQL knowledge
- Notes: Add user add/delete/edit functions and any others which are relevant to the effort

ASSIGNEE: matthew-silva

# User Story #15

## Add Database Table for facility info

- TODO

# User Story #16

## Add Database Table for admin users

- TODO

# User Story #17

## Create Database Functions Specific to Organized Storage Facility Data Management

- TODO

# User Story #18

## Create Database Functions Specific to Organized Storage Admin User Management

- TODO
