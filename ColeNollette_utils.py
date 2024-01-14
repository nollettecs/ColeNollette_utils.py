""" This module provides a reusable byline for the author's services. """

#Byline string

byline: str = f"""
{company_name}
{active_projects_string}
{international_prescence_string}
{client_satisfaction_string}
{services_offered}
{satisfaction_score}
"""

#Imports

import math
import statistics

#Variables

company_name: str = "Tech Driven Data LLC."
count_active_projects: int = 6
has_international_prescence: bool = False
average_client_satisfaction: float = 4.8
services_offered: list = ["Data Analysis", "Python programming", "Data Science", "Data Cleaning"]
satisfaction_score: list = [4.9, 4.8, 4.8, 4.7, 4.6, 5.0]

#Formatted strings

company_name_string: str = f"Company Name: {company_name}"
active_projects_string: str = f"Active projects: {count_active_projects}"
international_prescence_string: str = f"Internation prescence: {has_international_prescence}"
client_satisfaction_string: str = f"Average client satisfaction: {average_client_satisfaction}"

#Descriptive statistics

smallest = min(satisfaction_score)
largest = max(satisfaction_score)
total = sum(satisfaction_score)
count = len(satisfaction_score)
mean = statistics.mean(satisfaction_score)
mode = statistics.mode(satisfaction_score)
median = statistics.median(satisfaction_score)
standard_deviation = statistics.stdev(satisfaction_score)

def main():
    ''' Display all output'''
print(company_name)
print(active_projects_string)
print(international_prescence_string)
print(client_satisfaction_string)

#Not quite sure what I did wrong that lead me to having to print each statistic individually like this... Hopefully I'll get this figured out and changed!

print (byline)
print (smallest)
print (largest)
print (total)
print (count)
print (mean)
print (median)
print (mode)
print (standard_deviation)

if __name__ == '__main__':
    main()
