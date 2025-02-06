try:
    while True:
        projects = []  
        current_project = None
        current_students = set()
        while True:
            line = input().strip()
            if line == '0':
                exit()
            if line == '1':
                if current_project is not None:
                    projects.append((current_project, current_students))
                student_counts = {}
                for p_name, students in projects:
                    for student in students:
                        student_counts[student] = student_counts.get(student, 0) + 1
                project_counts = []
                for p_name, students in projects:
                    valid = 0
                    for student in students:
                        if student_counts[student] == 1:
                            valid += 1
                    project_counts.append((p_name, valid))
                sorted_projects = sorted(project_counts, key=lambda x: (-x[1], x[0]))
                for name, count in sorted_projects:
                    print(f"{name} {count}")
                break
            elif line.isupper():
                if current_project is not None:
                    projects.append((current_project, current_students))
                current_project = line
                current_students = set()
            else:
                current_students.add(line)
except EOFError:
    pass