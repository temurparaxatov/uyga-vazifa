def find_best_department(employees):
    department_bonus_count = {}

    for employee in employees:
        name, position, salary, bonus, department = employee.split()
        bonus = int(bonus)
        department = department.split('-')[0]

        if bonus > 0:
            if department in department_bonus_count:
                department_bonus_count[department] += 1
            else:
                department_bonus_count[department] = 1

    max_count = max(department_bonus_count.values())
    best_departments = [dept for dept, count in department_bonus_count.items() if count == max_count]

    return best_departments

inputs = [
    [
        "Anvar Junior 500 100 1-bo'lim",
        "Asror Middle 1500 500 2-bo'lim",
        "Kamola Senior 2500 -100 3-bo'lim",
        "Vali Junior 500 -100 1-bo'lim",
        "Davron Middle 1500 100 2-bo'lim",
        "Bahodir Senior 2500 -100 3-bo'lim",
        "Farrux Junior 500 100 1-bo'lim",
        "Jamila Middle 1500 200 2-bo'lim",
        "Jasur Senior 2500 -100 3-bo'lim",
        "Komila Junior 500 -100 1-bo'lim"
    ],
    [
        "Anvar Junior 500 -100 1-bo'lim",
        "Asror Middle 1500 500 2-bo'lim",
        "Kamola Senior 2500 100 3-bo'lim",
        "Vali Junior 500 -100 1-bo'lim",
        "Davron Middle 1500 100 2-bo'lim",
        "Bahodir Senior 2500 100 3-bo'lim",
        "Farrux Junior 500 -100 1-bo'lim",
        "Jamila Middle 1500 200 2-bo'lim",
        "Jasur Senior 2500 100 3-bo'lim",
        "Komila Junior 500 -100 1-bo'lim"
    ]
]

for employees in inputs:
    best_departments = find_best_department(employees)
    for department in best_departments:
        print(f"{department}-bo'lim")
    print()  
