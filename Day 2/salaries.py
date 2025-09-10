#Using debugger to debug the code
#Inserting the break points

def find_min(salaries):
    min_salary  = salaries[0]
    for salary in salaries:
        if salary < min_salary:
            min_salary = salary
    return min_salary

def find_max(salaries):
    max_salary = salaries[0]
    for salary in salaries:
        if salary > max_salary:
            max_salary = salary
    return max_salary

def find_total(salaries):
    total = 0
    for salary in salaries:
        total += salary
    return total

#Driver code
salaries = [1000, 2000, 3000, 4000, 5000]
min_salary = find_min(salaries)
max_salary = find_max(salaries)
total_salary = find_total(salaries)
print(f'Min Salary: {min_salary}\nMax Salary: {max_salary}\nTotal Salary: {total_salary}')
