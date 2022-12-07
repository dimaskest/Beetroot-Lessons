import sqlite3
import contextlib
import pandas as pd
from tabulate import tabulate


class LocalSQLiteDB:
    def __init__(self, database_name: str):
        self.database = database_name
    
    def __execute_command_query(self, query: str):
        with contextlib.closing(sqlite3.connect(self.database)) as self.conn:  # auto-closes
            with self.conn:  # auto-commits
                with contextlib.closing(self.conn.cursor()) as self.cursor:  # auto-closes
                    self.cursor.execute(query)

    def __execute_select(self, query: str):
        with contextlib.closing(sqlite3.connect(self.database)) as self.conn:  # auto-closes
            with self.conn:  # auto-commits
                with contextlib.closing(self.conn.cursor()) as self.cursor:  # auto-closes
                    return self.cursor.execute(query).fetchall()

    def __execute_insert(self, query: str, data: tuple):
        with contextlib.closing(sqlite3.connect(self.database)) as self.conn:  # auto-closes
            with self.conn:  # auto-commits
                with contextlib.closing(self.conn.cursor()) as self.cursor:  # auto-closes
                    self.cursor.execute(query, data)

    def __execute_multiple_insert(self, query: str, data: list):
        with contextlib.closing(sqlite3.connect(self.database)) as self.conn:  # auto-closes
            with self.conn:  # auto-commits
                with contextlib.closing(self.conn.cursor()) as self.cursor:  # auto-closes
                    self.cursor.executemany(query, data)
    def command_query(self, query: str):
        self.__execute_command_query(query)

    def drop_table(self, tablename: str):
        self.__execute_command_query(f"DROP TABLE IF EXISTS {tablename}")

    def show_tables(self):
        tabels = self.__execute_select("""
                    SELECT name FROM sqlite_schema
                    WHERE type='table'
                    ORDER BY name;
                    """)

        tabelsname_array = []
        records_num_array = []
        columns_num_array = []
        columns_names_array = []

        for tabel in tabels:
            tablename = tabel[0]
            tabelsname_array.append(tablename)

            records_num = self.__execute_select(f"SELECT COUNT(*) FROM {tablename}")[0][0]
            records_num_array.append(records_num)

            columns_names = [column_name[1] for column_name in
                             self.__execute_select(f"pragma table_info({tablename});")]
            columns_names_array.append(str(columns_names))

            columns = self.__execute_select(f"pragma table_info({tablename});")
            columns_num = len(columns)
            columns_num_array.append(columns_num)

        return pd.DataFrame({"tablename": tabelsname_array, "records_num": records_num_array,
                             "columns_num": columns_num_array, "columns_names": columns_names_array})
    
    def sqlQuery(self, query: str, return_pandas=True):

        if return_pandas:
            self.conn = sqlite3.connect(self.database)
            query_execution_result = pd.read_sql(query, self.conn)
            self.conn.close()
        else:
            query_execution_result = self.__execute_select(query)
        return query_execution_result

    def __insert_values_string(self, columns_num: int):
        if columns_num == 1:
            return "?"
        elif columns_num > 1:
            string = "?, " * columns_num
            string = string[:-2]
            return string

    def insert(self, tablename: str, data: list):
        columns = self.__execute_select(f"pragma table_info({tablename});")
        columns_num = len(columns)

        insert_values_string = self.__insert_values_string(columns_num)
        self.__execute_multiple_insert(f"INSERT or IGNORE INTO {tablename} VALUES({insert_values_string});", data)

        print("INSERTING COMPLETED 100%")


hr_database = LocalSQLiteDB("hr.db")

# print(tabulate(hr_database.sqlQuery("""
#     SELECT 
#         e.first_name, e.last_name, e.department_id, d.department_name 
#     FROM 
#         employees AS e 
#     LEFT JOIN department AS d
#         ON e.department_id = d.department_id
# """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT 
#         e.first_name, e.last_name, d.department_name, l.city, l.state_province
#     FROM
#         employees AS e 
#     LEFT JOIN department as d
#         ON e.department_id = d.department_id
#     LEFT JOIN locations as l
#         ON d.location_id = l.location_id
# """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT 
#         e.first_name, e.last_name, d.department_id, d.department_name, l.city, l.state_province
#     FROM
#         employees AS e 
#     LEFT JOIN department as d
#         ON e.department_id = d.department_id 
#     LEFT JOIN locations as l
#         ON d.location_id = l.location_id
#     WHERE d.department_id = 40 OR d.department_id = 80
# """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT department_name FROM department     
# """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT
#         e.first_name AS "Employee Name", m.first_name AS "Manager"
#     FROM employees as e 
#     JOIN employees as m
#         ON e.manager_id = m.employee_id
# """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT
#         e.first_name AS "Employee Name", m.first_name AS "Manager"
#     FROM employees as e 
#     JOIN employees as m
#         ON e.manager_id = m.employee_id
# """)))

# print(hr_database.sqlQuery("""
#     SELECT
#         j.job_title, e.first_name, e.last_name, j.max_salary-j.min_salary AS "Difference"
#     FROM 
#         employees AS e
#     LEFT JOIN jobs as j
#         ON e.job_id = j.job_id
# """))

# print(hr_database.sqlQuery("""
#     SELECT
#         j.job_title, e.first_name, e.last_name, j.max_salary-e.salary AS "Difference"
#     FROM 
#         employees AS e
#     LEFT JOIN jobs as j
#         ON e.job_id = j.job_id
# """))

# print(hr_database.sqlQuery("""
#     SELECT 
#         job_title, AVG(salary) 
#     FROM
#         employees 
#     NATURAL JOIN jobs 
#     GROUP BY 
#         job_title
# """))

# print(hr_database.sqlQuery("""
#     SELECT first_name, last_name, salary
# 	FROM employees
# 		JOIN departments USING (department_id)
# 		JOIN  locations USING (location_id)
# 	WHERE  city = 'London'
# """))

# print(hr_database.sqlQuery("""
#     SELECT 
#         d.department_name, e.*
#     FROM department AS d
#     JOIN
#     (SELECT count(employee_id), department_id FROM employees GROUP BY department_id) AS e USING (department_id)
# """))

# print(hr_database.show_tables())