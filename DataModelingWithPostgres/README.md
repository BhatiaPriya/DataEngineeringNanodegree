# Project: Data Modeling with Postgres

## Introduction:

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They want me to create a Postgres database with tables designed to optimize queries on song play analysis. My role is to create a database schema and ETL pipeline for this analysis. I should be able to test the database and ETL pipeline by running queries given by the analytics team from Sparkify and compare the results with their expected results.

## Project Description:

In this project, I'll apply what I've learnt on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, I will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Process: 

### Here is the descripition of each file used 

sql_queries.py:
contains all the queries used in the ETL pipeline

create_tables.py:
creates database and tables

etl.py: 
reads json files and loads the data into various tables. In other words, this file processes entire dataset and develops ETL process for each table 

test.ipynb:
tests that records were successfully inserted into each table

README.md: 
explains the completed project in short

## Dataset:

### Song Dataset:
Here is an example of how one of the files of song dataset looks like:

{"num_songs": 1,
 "artist_id": "ARJIE2Y1187B994AB7",
 "artist_latitude": null,
 "artist_longitude": null,
 "artist_location": "",
 "artist_name": "Line Renaud",
 "song_id": "SOUPIRU12A6D4FA1E1",
 "title": "Der Kleine Dompfaff",
 "duration": 152.92036,
 "year": 0
}

### Log Dataset:
Here is an example of how one of the files of log dataset looks like:

{"artist":"Des'ree",
 "auth":"Logged In",
 "firstName":"Kaylee",
 "gender":"F",
 "itemInSession":1,
 "lastName":"Summers",
 "length":246.30812,
 "level":"free",
 "location":"Phoenix-Mesa-Scottsdale, AZ",
 "method":"PUT","page":"NextSong",
 "registration":1540344794796.0,
 "sessionId":139,
 "song":"You Gotta Be",
 "status":200,
 "ts":1541106106796,
 "userAgent":"\"Mozilla\/5.0 (Windows NT 6.1; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/35.0.1916.153 Safari\/537.36\"",
 "userId":"8"
 }
 
## Schema for Song Play Analysis
Using the song and log datasets, I've created a star schema optimized for queries on song play analysis. This includes the following tables.

### Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong

various columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
users - users in the app

various columns: user_id, first_name, last_name, gender, level

songs - songs in music database

various columns: song_id, title, artist_id, year, duration

artists - artists in music database

various columns: artist_id, name, location, latitude, longitude

time - timestamps of records in songplays broken down into specific units

various columns: start_time, hour, day, week, month, year, weekday