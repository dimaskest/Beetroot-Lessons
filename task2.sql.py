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
#     SELECT employees.first_name, employees.last_name FROM employees 
#     ORDER BY last_name
#     """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT DISTINCT department_id FROM employees
#     ORDER BY department_id
#     """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT * FROM employees
#     ORDER BY first_name DESC
#     """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT 
#         employees.first_name, employees.last_name, employees.salary, employees.salary*.12 PF
#     FROM
#         employees
# """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT min(salary), max(salary) FROM employees
# """)))

# print(tabulate(hr_database.sqlQuery("""
#     SELECT employees.first_name, employees.last_name, employees.salary/12
#     FROM employees
#     ORDER BY salary
# """)))

# print(hr_database.show_tables())