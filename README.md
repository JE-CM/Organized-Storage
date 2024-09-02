# Organized-Storage

## Purpose

Create software which will manage user data for a cooperative self-storage facility.<br>
The project involves developing a comprehensive application featuring both a front end and back end to offer a streamlined self-storage management service. This application will support functionalities for storing and managing user data and packages in designated storage units. It will incorporate DevOps practices to handle aspects such as (automated deployment, continuous integration/continuous deployment (CI/CD) pipelines, and container orchestration), leverage data science techniques to (predict storage capacity utilization and demand for various facility responsibilities), and ensure basic security measures to (protect user data and maintain secure access control).

## Best Practices

### Reuse

The purpose of this program is quite specific: Creating a system which can manage the user data of a cooperative self-storage facility. However, the actual functionality will probably be quite useful for many different purposes. For this reason, we should put effort into making the basic functionality of the program quite reusable. The best way to do this will be to try our best to completely separate the business logic from the basic functionality. Often this can be achieved through modular design and using first-class functions.

## Design

### Front End

##### Requirements

- The front end shall be developed in bash.<br>
- The front end shall allow a user to edit their own user data
- The front end shall allow an admin user to edit any user's data.
- The front end shall use public key authentication to prove the user's identity
.
- The front end shall acess the back end CRUD interface for a user's data
.
- The front end shall acess the back end CRUD interface for the facility data

#### Note

*The front end should be extensible with a user-provided script that allows making use of existing commands in an automated fashion.<br> The front end should allow the setup of cron jobs to automatically run one or more commands at a specific time of day.<br>
The front end should remind the user of their facility responsibilities*

### Back End

#### Requirements

- The back end shall be written in python.
- The back end shall be an interface between the bash front end and the SQLite database.
- The back end shall have CRUD functionality for user records.
- The back end shall use public key authentication to prove the user's identity.
- The back end shall provide a CRUD interface for a user's data, which shall include their name, location in latitude/longitude coordinates, start storage date, end storage date, storage capacity used, and facility responsibilities (selected from a list of 4 options, inlcuding [cleaning, construction, maintenance, electrical]).
- The back end shall provide a CRUD interface for a the facility data, which shall include the facility storage capacity, facility responsibility demand (categorized from a list of 4 options, inlcuding [cleaning, construction, maintenance, electrical]), only accessible to admin user

##### Note
The back end should be deployed on a docker container.<br>
The docker container should be managed by k8s.<br>
The docker containers should be load-balanced in k8s.<br>
The back end should expose and be accessible by an http/https API with CRUD functionality.

### Database

* The user data shall be stored in a sqlite database.

>>Consider optimizing database queries and storage to handle large volumes of data.

### Data Science

We should use data science analysis techniques to predict on whether the storage facility is expected to reach capacity or reach a demand of over 100 in any of the 4 responsibility categories. A warning will be printed to all users in the case that the facility's data will meet any of these conditions in one month or less.

* Corporate social responsibility (CSR):
  1. Environmental Responsibility
  1. Ethical/Human Rights Responsibility
  1. Philanthropic Responsibility
  1. Economic Responsibility

### Cybersecurity
* Credentials and public keys protected and managed appropriately.

### Quality Assurance
* Perform tests to determine that the system can optimally handle the expected scalability

### Agile histories / Models
* https://drive.google.com/file/d/1cY8arNvlercgZCBvoxo6VhkztLkhYWCR/view?usp=sharing
