# Organized-Storage
Tecnologies
# Organized-Storage

## Purpose

Create software which will manage user data for a cooperative self-storage facility.

### Design

#### Front End

##### Requirements

. The front end shall be developed in bash.
. The front end shall allow a user to edit their own user data
. The front end shall allow an admin user to edit any user's data
. The front end shall use public key authentication to prove the user's identity
. The front end shall acess the back end CRUD interface for a user's data
. The front end shall acess the back end CRUD interface for the facility data

##### Recommendations

. The front end should be extensible with a user-provided script that allows making use of existing commands in an automated fashion
. The front end should allow the setup of cron jobs to automatically run one or more commands at a specific time of day
. The front end should remind the user of their facility responsibilities

#### Back End

##### Requirements

. The back end shall be written in python
. The back end shall be an interface between the bash front end and the sqlite database
. The back end shall have CRUD functionality for user records
. The back end shall use public key authentication to prove the user's identity
. The back end shall provide a CRUD interface for a user's data, which shall include their name, location in latitude/longitude coordinates, start storage date, end storage date, storage capacity used, and facility responsibilities (selected from a list of 4 options, inlcuding [cleaning, construction, maintenance, electrical])
. The back end shall provide a CRUD interface for a the facility data, which shall include the facility storage capacity, facility responsibility demand (categorized from a list of 4 options, inlcuding [cleaning, construction, maintenance, electrical]), only accessible to admin user

##### Recommendations

. The back end should be deployed on a docker container
. The docker container should be managed by k8s
. The docker containers should be load-balanced in k8s
. The back end should expose and be accessible by an http/https API with CRUD functionality

#### Database

. The user data shall be stored in a sqlite database

#### Data Science

. We should use datascience anaylsis techniques to predict on whether the storage facility is expected to reach capacity or reach a demand of over 100 in any of the 4 responsibility categories. A warning will be printed to all users in the case that the facility's data will meet any of these conditions in one month or less.

