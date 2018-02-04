"""Build redmine object and function for updating the server"""

from redmine import Redmine

url = input('Enter your project url: ')
api_key = open('api_key.txt','r')

redmine = Redmine(url, key=api_key)

def update_server(hours, comments):
	for index in range(0, len(projects)):
		time_entry = redmine.time_entry.create(
			project_id=counter(),
			spent_on=date,
			hours=int(hours[index]),
			comments=comments[index]
		)



"""Handle project id of new time entry resources"""

## Project id should start at 1 then increment with each new resource
count = 1

def counter():
	global count
	return count
	count = count + 1



"""Parse YAML for use in creating the time entry resource"""

from yaml import load

def parse_yaml(yaml_file):
	activities = load(yaml_file)
	hours = []
	comments = []
	for index in range(0, len(activities)):
		project_key = activities[index].keys()[0]
		hours.append(activities[index][project_key]['hours'])
		comments.append(activities[index][project_key]['comments'])
	update_server(hours, comments)



"""Verify that date is given and that it exists"""

import os, sys

## If date is not given, tell user to give date
try:
	date = sys.argv[1]
except IndexError:
	print("Error: Please enter date argument with format YYYY-MM-DD")



"""Access YAML files"""

def inspect_folder():
	if os.path.isdir(str(date)):
		if os.path.exists(str(date) + "/bj.yaml"):
			yaml_file_path = str(date) + "/bj.yaml"
			opened_yaml_file = open(yaml_file_path, 'r')
			parse_yaml(opened_yaml_file)
		if os.path.exists(str(date) + "/brandon.yaml"):
			yaml_file_path = str(date) + "/brandon.yaml"
			opened_yaml_file = open(yaml_file_path, 'r')
			parse_yaml(opened_yaml_file)
		if os.path.exists(str(date) + "/jesse.yaml"):
			yaml_file_path = str(date) + "/jesse.yaml"
			opened_yaml_file = open(yaml_file_path, 'r')
			parse_yaml(opened_yaml_file)
	else:
		## If invalid date is given, tell user to give a valid date
		print("Error: Please re-enter date with format YYYY-MM-DD")



"""Launch program"""

if __name__ == "__main__":
	inspect_folder()