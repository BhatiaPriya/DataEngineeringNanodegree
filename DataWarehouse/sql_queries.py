import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES
staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
staging_events_table_create= ("""
CREATE TABLE staging_events(
    artist VARCHAR,
    auth VARCHAR,
    firstName VARCHAR,
    gender VARCHAR,
    itemInSession INT,
    lastName VARCHAR,
    length NUMERIC,
    level VARCHAR,
    location VARCHAR,
    method VARCHAR,
    page VARCHAR,
    registration NUMERIC,
    sessionId INT,
    song VARCHAR,
    status INT,
    ts BIGINT,
    userAgent VARCHAR,
    userId INT
)
""")

staging_songs_table_create = ("""
CREATE TABLE staging_songs(
    num_songs INT,
    artist_id VARCHAR,
    artist_latitude NUMERIC,
    artist_longitude NUMERIC,
    artist_location VARCHAR,
    artist_name VARCHAR,
    song_id VARCHAR,
    title VARCHAR,
    duration NUMERIC,
    year INT
)
""")

# The SERIAL command in Postgres is not supported in Redshift. The equivalent in redshift is IDENTITY(0,1)
songplay_table_create = ("""
CREATE TABLE songplays(
    songplay_id INT IDENTITY(0,1) PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    level VARCHAR,
    song_id VARCHAR NOT NULL,
    artist_id VARCHAR NOT NULL,
    session_id INT,
    location VARCHAR,
    user_agent VARCHAR
)
""")

user_table_create = ("""
CREATE TABLE users(
    user_id INT PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    level VARCHAR
)
""")

song_table_create = ("""
CREATE TABLE songs(
    song_id VARCHAR PRIMARY KEY,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration NUMERIC
)
""")

artist_table_create = ("""
CREATE TABLE artists(
    artist_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    location VARCHAR,
    lattitude NUMERIC,
    longitude NUMERIC
)
""")

time_table_create = ("""
CREATE TABLE time(
    start_time TIMESTAMP PRIMARY KEY,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday INT
)
""")

# STAGING TABLES
staging_events_copy = ("""
copy staging_events
    from {}
    iam_role {}
    json {}
""").format(config['S3']['LOG_DATA'], config['IAM_ROLE']['arn'], config['S3']['LOG_JSONPATH'])

staging_songs_copy = ("""
copy staging_songs
    from {}
    iam_role {}
    json 'auto'
""").format(config['S3']['SONG_DATA'], config['IAM_ROLE']['ARN'])

# FINAL TABLES
# Redshift doesnt have the from_unixtime() function. we need to use the below sql query to get the timestamp. It just adds the no of seconds to epoch and returns as timestamp
# epoch: For date and timestamp values, the number of seconds since 1970-01-01 00:00:00 UTC (can be negative); for interval values, the total number of seconds in the interval
# Here is how we can convert an epoch value back to a timestamp (ts is an epoch here)[Ref 1]

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    SELECT DISTINCT
            timestamp 'epoch' + (se.ts/1000) * interval '1 second',
            se.userId,
            se.level,
            ss.song_id,
            ss.artist_id,
            se.sessionId,
            se.location,
            se.userAgent
    FROM staging_events se
    JOIN staging_songs ss
    ON se.artist = ss.artist_name AND se.length = ss.duration AND se.song = ss.title
    WHERE page = 'NextSong'
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level)
    SELECT DISTINCT
             userId,
             firstName,
             lastName,
             gender,
             level
    FROM staging_events
    WHERE page = 'NextSong'
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration)
    SELECT DISTINCT
             song_id,
             title,
             artist_id,
             year,
             duration
    FROM staging_songs
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, lattitude, longitude)
    SELECT DISTINCT
             artist_id,
             artist_name,
             artist_location,
             artist_latitude,
             artist_longitude
    FROM staging_songs
""")

time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday)
    SELECT DISTINCT
            timestamp 'epoch' + (se.ts/1000) * interval '1 second' AS start_time,
            EXTRACT (hour FROM start_time),
            EXTRACT (day FROM start_time),
            EXTRACT (week FROM start_time),
            EXTRACT (month FROM start_time),
            EXTRACT (year FROM start_time),
            EXTRACT (weekday FROM start_time)
    FROM staging_events se
""")

# QUERY LISTS
create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
