### Introduction of the Project:
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

My task is to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. I should be able to test the database and ETL pipeline by running queries given to me by the analytics team from Sparkify and compare the results with their expected results.

### Project Description:
In this project, I will apply what I've learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, I will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

### Description of the files used:

1. dwh.cfg: It's a configuration file. Contains redshift cluster and IAM role information
2. create_tables.py: creates staging, fact and dimension tables
3. sql_queries.py: contains all the queries used in the ETL pipeline
4. etl.py: reads json files and loads the data into various tables
5. README.md: explains the completed project in short

### Dataset (both of the datasets reside in aws, s3 bucket):

#### Song Dataset:
Here is an example of how one of the files of song dataset looks like:

{
"num_songs": 1,
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

#### Log Dataset:
Here is an example of how one of the files of log dataset looks like:

{
"artist":"Des'ree",
"auth":"Logged In", 
"firstName":"Kaylee",
"gender":"F",
"itemInSession":1,
"lastName":"Summers", 
"length":246.30812, 
"level":"free", 
"location":"Phoenix-Mesa-Scottsdale, AZ",
"method":"PUT",
"page":"NextSong",
"registration":1540344794796.0,
"sessionId":139, "song":"You Gotta Be", 
"status":200, 
"ts":1541106106796,
"userAgent":""Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"",
"userId":"8" 
}

### Various tables used:

#### Fact Table:
songplays - records in log data associated with song plays i.e. records with page NextSong various columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

#### Dimension Tables:
users - users in the app various columns: user_id, first_name, last_name, gender, level

songs - songs in music database various columns: song_id, title, artist_id, year, duration

artists - artists in music database various columns: artist_id, name, location, latitude, longitude

time - timestamps of records in songplays broken down into specific units various columns: start_time, hour, day, week, month, year, weekday

### References:
1. https://stackoverflow.com/questions/39815425/how-to-convert-epoch-to-datetime-redshift