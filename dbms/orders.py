import sqlite3
import datetime

DATABASE_NAME = 'orders.db'

def connect_to_database():
    return sqlite3.connect(DATABASE_NAME, check_same_thread=False)

def reset_back_to_start():
    with connect_to_database() as conn:
        c = conn.cursor()
        print("[WARNING!] You need admin privilege to clear and reset the data! Are you sure? (y/n/yes/no)")
        a = input()
        c.execute("DROP TABLE IF EXISTS orders")
        if a in ("y", "yes"):
            c.execute('''CREATE TABLE IF NOT EXISTS orders
                        (orderid INTEGER PRIMARY KEY AUTOINCREMENT,
                        order_date_time TEXT DEFAULT CURRENT_TIMESTAMP,
                        address TEXT DEFAULT NULL,
                        payment_method TEXT CHECK(payment_method IN ('upi', 'cash_on_delivery')),
                        paid BOOLEAN DEFAULT FALSE
                        )''')

def insert_order(address, payment_method, paid=False):
    with connect_to_database() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO orders (address, payment_method, paid) VALUES (?, ?, ?)",
                  (address, payment_method, paid))

def read_orders():
    with connect_to_database() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM orders")
        result = c.fetchall()
    return result

def read_order_by_id(order_id):
    with connect_to_database() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM orders WHERE orderid=?", (order_id,))
        result = c.fetchone()
    return result

def update_order(order_id, address=None, payment_method=None, paid=None):
    with connect_to_database() as conn:
        c = conn.cursor()

        update_query = "UPDATE orders SET "
        update_values = []

        if address is not None:
            update_query += "address=?, "
            update_values.append(address)

        if payment_method is not None:
            update_query += "payment_method=?, "
            update_values.append(payment_method)

        if paid is not None:
            update_query += "paid=?, "
            update_values.append(paid)

        # Remove the trailing comma and space
        update_query = update_query.rstrip(", ")

        # Add the WHERE clause to update based on the order ID
        update_query += " WHERE orderid=?"

        # Add the order ID value to the update_values list
        update_values.append(order_id)

        # Execute the update query
        c.execute(update_query, tuple(update_values))

# Example usage:
# reset_back_to_start()
# insert_order('123 Main St', 'cash_on_delivery')
# insert_order('456 Oak St', 'upi', paid=True)
# update_order(1, address='789 Pine St', payment_method='upi')
# orders = read_orders()
# specific_order = read_order_by_id(1)
