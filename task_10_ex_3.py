"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""


def get_top_performers(file_path, number_of_top_students=5):
    students_dict = {}

    with open(file_path, 'r') as inp_file:
        for line in inp_file.readlines():
            line = line.strip().split(',')
            if line[-1].replace('.', '', 1).isdigit():
                students_dict[line[0]] = float(line[-1])

    return sorted(students_dict.keys(), key=lambda x: students_dict[x], reverse=True)[:number_of_top_students]


def write_students_age_desc(file_path, output_file):
    lines = []

    with open(file_path, 'r') as inp_file:
        for line in inp_file.readlines():
            lines.append(line.strip())

    lines.sort(key=lambda x: float(y) if (y := x.split(',')[1]).isdecimal() else float('inf'), reverse=True)

    with open(output_file, 'w') as out_file:
        for line in lines:
            if line != lines[-1]:
                line += '\n'

            out_file.write(line)
