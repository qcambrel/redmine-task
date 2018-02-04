##  The Task

This is a programming exercises that I was assigned by a company that I interviewed with in the past. During this test, I learned about Redmine and the PyYAML libray and gained a better understanding of Python dictionaries, the os and sys modules, and the value of the principle of separation of concerns.

### The requirements were as follows:

The team needed to record roughly they worked on and the duration for which they worked on it. The team wanted an automated way of updating the logs instead to replace manually inputting the information through the web interface every week. This exercise entailed writing a program that will enter the weekly logs without the use of the web interface. I chose to implement my program in Python.

A dummy Redmine server was set up for the exercise. My code had to interface with the server using the Redmine API. I used an API key saved on a text file that is not included in this repo. For testing and set up, I logged in to Redmin using login credentials that are also excluded from this repo. After the entries were successfully posted, I would be able to see them under "Spent time" page.

There is a folder, again excluded from this repo, named after the date of the week. The folder contains the YAML files with names that match members of the dev team. A folder like this is created each week with the aforementioned date naming convention. Each file consists of the project name, hours worked, and comments of what was done. The only stipulation is that the hours worked are updated for the correct week. This program is used each week to log the hours and comments for the respective projects that were worked on.