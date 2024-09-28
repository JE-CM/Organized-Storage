# Organized-Storage

## Purpose

Create software which will manage user data for a cooperative self-storage facility.<br>
The project involves developing a comprehensive application featuring both a front end and back end to offer a streamlined self-storage management service. This application will support functionalities for storing and managing user data and packages in designated storage units. It will incorporate DevOps practices to handle aspects such as (automated deployment, continuous integration/continuous deployment (CI/CD) pipelines, and container orchestration), leverage data science techniques to (predict storage capacity utilization and demand for various facility responsibilities), and ensure basic security measures to (protect user data and maintain secure access control).

## Topic

> The online platform is designed to interact with "self storage facility" catering to clients such as companies and individuals looking to store items in different sized storage units. We will oversee three categories. Smalls ones for items and larger ones, for bulkier belongings. Each category will offer features tailored to suit the needs of different clients and circumstances.

## Front End

### Requirements

The front end shall have:

- Being developed in bash.<br>
- Allow a user to edit their own user data.
- Allow an admin user to edit any user's data.
- Use public key authentication to prove the user's identity.
- Acess the back end CRUD interface for a user's data.
- Aess the back end CRUD interface for the facility data.

#### Note

- _The front end should be extensible with a user-provided script that allows making use of existing commands in an automated fashion._<br>
- _The front end should allow the setup of cron jobs to automatically run one or more commands at a specific time of day._<br>
- _The front end should remind the user of their facility responsibilities_

## Back End

### Requirements

The back end shall have:

- Be written in python.
- Be an interface between the bash front end and the SQLite database.
- Have CRUD functionality for user records.
- Use public key authentication to prove the user's identity.
- Provide a CRUD interface for a user's data, which shall include their name, location in latitude/longitude coordinates, start storage date, end storage date, storage capacity used, and facility responsibilities (selected from a list of 4 options, inlcuding [cleaning, construction, maintenance, electrical]).
- Provide a CRUD interface for a the facility data, which shall include the facility storage capacity, facility responsibility demand (categorized from a list of 4 options, inlcuding [cleaning, construction, maintenance, electrical]), only accessible to admin user

#### Note

The back end should be deployed on a docker container.<br>
The docker container should be managed by k8s.<br>
The docker containers should be load-balanced in k8s.<br>
The back end should expose and be accessible by an http/https API with CRUD functionality.

## Database

The user data shall be stored in a sqlite database.

> Consider optimizing database queries and storage to handle large volumes of data.
