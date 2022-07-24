import sqlite3
import re

names = ["David", "Konstantin", "Sergeeva", "David", "Konstantin", "Sergeeva"]
job_id = ["dvornik", "manager", "IT_PROG", "dvornik", "manager", "IT_PROG"]
salary = [3000, 10000, 20000, 37000, 10010, 203000]
department_id = [50, 50, 27, 50, 44, 450]
data_job = ["2020-07-26", "2021-07-26", '2022-07-26', "2020-02-26", "2021-08-26", '2022-01-26']
manager_id = ["Karina", "Matilda", "Karina", "Karina", "Karina", "Karina"]

db = sqlite3.connect("BD.db")

c = db.cursor()

c.execute('''CREATE TABLE Employees(
    id INTEGER PRIMARY KEY,
    names VARCHAR(15),
    job_id VARCHAR(15),
    salary INT,
    department_id INT,
    data_job DATE,
    manager_id VARCHAR(15)
)''')

for i in range(len(names)):
    c.execute('''INSERT INTO Employees VALUES (NULL, '%s' ,'%s', %d, %d, '%s','%s')
    ''' % (names[i], job_id[i], salary[i],department_id[i], data_job[i], manager_id[i]))
with open('BD.db') as baza:
    c.execute('SELECT * FROM Employees')
    info = c.fetchall()
    for el in info:
        print(list(el))
print("==========================================================================================")

# Вывести список Давидов
c.execute('SELECT id, job_id, names FROM Employees WHERE names = "David"')
print(c.fetchall())
print("==========================================================================================")

# IT_PROG
c.execute('SELECT id, job_id, names FROM Employees WHERE job_id = "IT_PROG"')
print(c.fetchall())
print("==========================================================================================")

# dep_ID 50 salary>4000
c.execute('SELECT * FROM Employees WHERE department_id == 50 and salary > 4000')
print(c.fetchall())
print("==========================================================================================")

# name ______a
c.execute('SELECT id, names FROM Employees ')
name_a = c.fetchall()
print(name_a)
for i in name_a:
    for el in i:
        if re.findall("a\Z", str(el)):
            print(i)
print("==========================================================================================")

# n>2 for names
for i in name_a:
    for el in i:
        if len(re.findall(r'n', str(el))) > 1:
            print(i)

print("==========================================================================================")


c.execute('''SELECT department_id,
    MIN (salary) min_salary,
    MAX (salary) max_salary,
    MIN (data_job) min_hire_date,
    MAX (data_job) max_hire_Date,
    COUNT (*) count
    FROM employees
    GROUP BY department_id order by count(*) desc;''')

print(c.fetchall())

c.execute('''SELECT manager_id, SUM (salary) as sum_salary
    FROM employees
	GROUP BY manager_id
  	HAVING COUNT (*) >= 5 AND SUM (salary) > 50000;''')

print(c.fetchall())

print("==========================================================================================")


db.commit()
db.close()

