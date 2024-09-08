import sqlite3

DATABASE = 'coffee_shop.db'

def get_connection():
    """Get a connection to the SQLite database."""
    return sqlite3.connect(DATABASE)

def initialize_db():
    """Create tables and insert sample data into the database."""
    conn = get_connection()
    cursor = conn.cursor()

    # Execute SQL queries to create tables and insert sample data
    with open('queries.sql', 'r') as file:
        sql_script = file.read()
        cursor.executescript(sql_script)

    conn.commit()
    conn.close()

def create_order(customer_id, coffee_id, price):
    """Create a new order in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO Orders (customer_id, coffee_id, price) 
        VALUES (?, ?, ?)
    """, (customer_id, coffee_id, price))
    
    conn.commit()
    conn.close()

def get_orders_for_coffee(coffee_id):
    """Retrieve all orders for a specific coffee."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Orders WHERE coffee_id = ?", (coffee_id,))
    results = cursor.fetchall()
    
    conn.close()
    return results

def get_customers_for_coffee(coffee_id):
    """Retrieve distinct customers who have ordered a specific coffee."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT DISTINCT Customers.* 
        FROM Customers 
        JOIN Orders ON Customers.id = Orders.customer_id 
        WHERE Orders.coffee_id = ?
    """, (coffee_id,))
    results = cursor.fetchall()
    
    conn.close()
    return results

def get_orders_for_customer(customer_id):
    """Retrieve all orders for a specific customer."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Orders WHERE customer_id = ?", (customer_id,))
    results = cursor.fetchall()
    
    conn.close()
    return results

def get_coffees_for_customer(customer_id):
    """Retrieve distinct coffees ordered by a specific customer."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT DISTINCT Coffees.* 
        FROM Coffees 
        JOIN Orders ON Coffees.id = Orders.coffee_id 
        WHERE Orders.customer_id = ?
    """, (customer_id,))
    results = cursor.fetchall()
    
    conn.close()
    return results

def get_num_orders_for_coffee(coffee_id):
    """Retrieve the number of orders for a specific coffee."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM Orders WHERE coffee_id = ?", (coffee_id,))
    count = cursor.fetchone()[0]
    
    conn.close()
    return count

def get_average_price_for_coffee(coffee_id):
    """Retrieve the average price for a specific coffee."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT AVG(price) 
        FROM Orders 
        WHERE coffee_id = ?
    """, (coffee_id,))
    avg_price = cursor.fetchone()[0]
    
    conn.close()
    return avg_price if avg_price is not None else 0

def get_customer_most_spent_on_coffee(coffee_id):
    """Retrieve the customer who spent the most on a specific coffee."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Customers.id, Customers.name, SUM(Orders.price) AS total_spent
        FROM Customers
        JOIN Orders ON Customers.id = Orders.customer_id
        WHERE Orders.coffee_id = ?
        GROUP BY Customers.id, Customers.name
        ORDER BY total_spent DESC
        LIMIT 1
    """, (coffee_id,))
    result = cursor.fetchone()
    
    conn.close()
    return result
