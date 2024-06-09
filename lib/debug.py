from __init__ import CONN, CURSOR
from department import Department

# import ipdb


def reset_database():
    Department.drop_table()
    Department.create_table()

    Department.create("Payroll", "Building A, 5th Floor")
    Department.create("Human Resources", "Building C, East Wing")
    Department.create("Accounting", "Building B, 1st Floor")

# reset_database()
# print(Department.all)

# row = CURSOR.execute("SELECT * FROM departments").fetchone()
# department = Department.instance_from_db(row)
# print(department)

print(Department.get_all())

# ipdb.set_trace()