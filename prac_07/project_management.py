"""CP1404/CP5632 Practical
Project Management Program! :
Estimate: 255 19:38-10:40 9:47-  minutes
Actual:   minutes
"""
import datetime
import csv
from collections import namedtuple

from macholib.mach_o import rpath_command

from project import Project

MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

def main():
    projects = None
    print("Welcome to Pythonic Project Management")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            projects = load_project()
        elif menu_choice == "S":
            pass
        elif menu_choice == "D":
            if projects:
                display_project(projects)
            else:
                print("Projects not found")
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Thank you for using Pythonic Project Management")


def display_project(projects):
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    complete_projects.sort()
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    incomplete_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects:")
    for project in complete_projects:
        print(project, end='')





def load_project():
    """Prompt the user for a file name and load projects and load them"""
    # filename = input("Enter project file name: ")
    projects = []
    filename = "projects.txt"
    with open(filename, "r") as in_file:
        first_line = in_file.readline()
        #Break up data based on tab
        fields = first_line.strip().split("\t")
        fields_string = ",".join(fields)
        #Replace space in field names with underscore character
        fields_string = fields_string.replace(" ", "_")
        Project_fields = namedtuple("Project_fields", fields_string)
        for project_map_record in map(Project_fields._make, csv.reader(in_file, delimiter="\t")):
            date = datetime.datetime.strptime(project_map_record.Start_Date, "%d/%m/%Y").date()
            new_project =Project(project_map_record.Name, date, project_map_record.Priority, float(project_map_record.Cost_Estimate), int(project_map_record.Completion_Percentage))
            projects.append(new_project)
        return projects



main()

