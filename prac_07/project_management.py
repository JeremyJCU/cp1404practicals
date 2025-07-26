"""CP1404/CP5632 Practical
Project Management Program! :
Estimate: 255 minutes
Actual:  736 minutes
"""
from datetime import datetime
import csv
from collections import namedtuple

from project import Project

INPUT_ERROR = "Invalid choice"
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
    project_headers = ""
    projects = None
    print("Welcome to Pythonic Project Management")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            projects, project_headers = load_project()
        elif menu_choice == "S":
            save_project(projects, project_headers)
        elif menu_choice == "D":
            if projects:
                sort_complete_projects(projects)
            else:
                print("Projects not found")
        elif menu_choice == "F":
            filter_by_date(projects)
        elif menu_choice == "A":
            projects = add_project(projects)
        elif menu_choice == "U":
            projects = update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Thank you for using Pythonic Project Management")


def filter_by_date(projects):
    """Filter projects that start after date and are sorted by date."""
    date = get_valid_date("Start date (dd/mm/yyyy): ", INPUT_ERROR)
    projects_after_date = [project for project in projects if project.start_date > date]
    # I wan't able to rind a way to do this using __lt__ or __gt__
    projects_after_date_post_sorted = sorted(projects_after_date, key=lambda project: project.start_date)
    display_projects(projects_after_date_post_sorted)


def get_valid_float(prompt, error, low):
    """Get valid float number from user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = float(input(prompt))
            if number < low:
                print(error)
            else:
                is_valid_input = True
        except ValueError:
            print(error)
    return number


def get_valid_date(prompt, error):
    """Get valid date input from user."""
    is_valid_date = False
    while not is_valid_date:
        try:
            string_date = input(prompt)
            date = convert_to_date(string_date)
            is_valid_date = True
        except ValueError:
            print(error)
    return date


def get_valid_string(prompt, error, empty_string):
    """Get valid input string entry."""
    string = input(prompt)
    while string == empty_string:
        print(error)
        string = input(prompt)
    return string


def get_valid_number(prompt, error, low, high):
    """Get valid input number."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number < low or number > high:
                print(error)
            else:
                is_valid_input = True
        except ValueError:
            print(error)
    return number


def add_project(projects):
    """Add a new project record."""
    print("Let's add a new project")
    name = get_valid_string("Name: ", INPUT_ERROR, "")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ", INPUT_ERROR)
    priority = get_valid_number("New Priority: ", INPUT_ERROR, 1, 10)
    cost_estimate = get_valid_float("Cost estimate: ", INPUT_ERROR, 0)
    completion_percentage = get_valid_number("New percentage: ", INPUT_ERROR, 0, 100)
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    projects.sort()
    return projects


def active_projects(projects):
    """Creates a list of active projects."""
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    incomplete_projects.sort()
    return incomplete_projects


def update_project(projects):
    """Updates a project record with new percentage and priority values."""
    incomplete_projects = active_projects(projects)
    for project_number, project in enumerate(incomplete_projects):
        print(f"{project_number + 1}: {project}")

    # Select a project to update
    project_choice = (get_valid_number("Project choice:", INPUT_ERROR, 0, len(incomplete_projects) + 1)) - 1

    # Save the selected project to a variable
    selected_project = incomplete_projects[project_choice]
    print(selected_project)

    # Enter a new percentage value
    new_percentage = get_valid_number("New percentage: ", INPUT_ERROR, 0, 100)
    selected_project.completion_percentage = new_percentage

    # Enter a new priority value
    new_priority = get_valid_number("New Priority: ", INPUT_ERROR, 1, 10)
    selected_project.priority = new_priority
    return projects


def display_projects(projects):
    """Display projects records."""
    for project in projects:
        print(project)


def sort_complete_projects(projects):
    """Filter two groups: incomplete projects; completed projects, both sorted by priority"""
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    complete_projects.sort()
    incomplete_projects = active_projects(projects)
    # Print incomplete projects
    print("Incomplete projects:")
    display_projects(incomplete_projects)
    # Print completed projects
    print("Completed projects:")
    display_projects(complete_projects)


def load_project():
    """Prompt the user for a file name and load projects and load them"""
    projects = []
    is_valid_input = False
    while not is_valid_input:
        try:
            filename = get_valid_string("Enter file to load ", INPUT_ERROR, "")
            with open(filename, "r") as in_file:
                first_line = in_file.readline()
                # Break up data based on tab
                fields = first_line.strip().split("\t")
                fields_string = ",".join(fields)
                # Replace space in field names with underscore character
                fields_string = fields_string.replace(" ", "_")
                Project_fields = namedtuple("Project_fields", fields_string)
                for project_map_record in map(Project_fields._make, csv.reader(in_file, delimiter="\t")):
                    date = convert_to_date(project_map_record.Start_Date)
                    new_project = Project(project_map_record.Name, date, int(project_map_record.Priority),
                                          float(project_map_record.Cost_Estimate),
                                          int(project_map_record.Completion_Percentage))
                    projects.append(new_project)
                is_valid_input = True
        except FileNotFoundError:
            print(INPUT_ERROR)
    print(f"{len(projects)} projects loaded.")
    return projects, first_line


def save_project(projects, project_headers):
    """Save projects records to file specified by user."""
    filename = input("Enter file name to save projects: ")
    with open(filename, "w") as out_file:
        print(project_headers, file=out_file, end="")
        for project in projects:
            print(repr(project), file=out_file)



def convert_to_date(string_date):
    """Convert a string date to datetime."""
    date = datetime.strptime(string_date, "%d/%m/%Y").date()
    return date


main()
