# Project: Data Modeling with Apache Cassandra

## Introduction:

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They want me to create an Apache Cassandra database which can create queries on song play data to answer the questions. My role is to create a database for this analysis. I should be able to test the database by running queries given by the analytics team from Sparkify to create the results.

## Project Description:

In this project, I'll apply what I've learnt on data modeling with Apache Cassandra and complete an ETL pipeline using Python. To complete the project, I will need to model the data by creating tables in Apache Cassandra to run queries. I was provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

## Process: 

### Here is the descripition of each file used 

project_file.ipynb:
this ia a jupyter notebook which reads all the csv files and creates Cassandra database

event_data folder:
source dataset(csv's) used in this project

event_datafile_new.csv:
a small event data csv file generated from the source event_data csv files. It was used to insert data into cassandra tables

README.md: 
explains the completed project in short

## Datasets

event_data which is the directory of CSV files partitioned by date. Here are examples of filepaths to two files in the dataset:

event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv

Here each csv file contains records of "song listening activities" by users of Sparkify mobile app