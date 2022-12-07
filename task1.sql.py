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

# 1: створюю таблицю store_sales в hr.db (база даних з уроку)

# sales_database.command_query("""
#     CREATE TABLE store_sales (
#         store_id INTEGER,
#         product_id INTEGER,
#         purchase_date TEXT,
#         quantity NUMERIC,
        
#         PRIMARY KEY(store_id, product_id, purchase_date)
# )
# """)

# 2: перейменовую її

# hr_database.command_query("""
#     ALTER TABLE store_sales
#     RENAME TO sales_store
# """)

# 3: Додаю стовбець sale_price

# hr_database.command_query("""
#     ALTER TABLE sales_store ADD sale_price NUMERIC
# """)

# 4: Вставляю рядок зі значеннями, одне з яких неправильне (дата)

# hr_database.command_query("""
#     INSERT INTO sales_store (store_id, product_id, purchase_date, quantity, sale_price) VALUES (1, 1, 10-10-2022, 10, 100)
# """)

# 5: Видаляю рядок з неправильним значенням

# hr_database.command_query("""
#     DELETE FROM sales_store WHERE store_id = 1
# """)

# 6: Додаю одразу два рядки зі значеннями

# hr_database.command_query("""
#     INSERT INTO sales_store (store_id, product_id, purchase_date, quantity, sale_price) 
#     VALUES (1, 1, '10.10.2022', 10, 100), 
#         (2, 2, '11.10.2022', 11, 110)
# """)

# 7: Апдейчу одне значення в одному рядку

# hr_database.command_query("""
#     UPDATE sales_store SET quantity = 20 WHERE quantity = 11
# """)

print(hr_database.sqlQuery("""
    SELECT * from sales_store
"""))