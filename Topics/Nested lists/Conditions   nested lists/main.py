"""Imagine you have a list of students and their grades for an exam:

students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]
Select only students with the best grade ("A") and print their names in a list. Do all this in one line. We have already created the students variable with other names and grades."""




# the list "students" is already defined

print([name_list[0] for name_list in students for name in name_list if name == "A"])