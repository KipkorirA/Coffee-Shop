
# Coffee Shop Database ~ Aron Kipkorir

This project consists of an SQLite database for managing a coffee shop's orders, customers, and coffee types. It includes SQL scripts for creating the database schema, a Python script for interacting with the database, and various SQL queries for retrieving and manipulating data.

## Project Structure

- `coffee_shop.db`: The SQLite database file that stores the coffee shop data.
- `create.sql`: SQL script to create tables in the `coffee_shop.db` database.
- `queries.sql`: SQL script containing various queries for retrieving and manipulating data.
- `db.py`: Python script for interacting with the database.
- `README.md`: This file.

## Setup

1. **Create the Database:**

   Run the `create.sql` script to set up the initial database schema. You can execute it using an SQLite client or through the Python script `db.py`.

2. **Initialize the Database:**

   Execute the `initialize_db()` function in `db.py` to create tables and insert sample data. This function reads and executes the SQL commands from `queries.sql`.

   ```python
   from db import initialize_db
   initialize_db()
   ```

## Functions in `db.py`

- `create_order(customer_id, coffee_id, price)`: Creates a new order in the database.
- `get_orders_for_coffee(coffee_id)`: Retrieves all orders for a specific coffee.
- `get_customers_for_coffee(coffee_id)`: Retrieves distinct customers who have ordered a specific coffee.
- `get_orders_for_customer(customer_id)`: Retrieves all orders for a specific customer.
- `get_coffees_for_customer(customer_id)`: Retrieves distinct coffees ordered by a specific customer.
- `get_num_orders_for_coffee(coffee_id)`: Retrieves the number of orders for a specific coffee.
- `get_average_price_for_coffee(coffee_id)`: Retrieves the average price for a specific coffee.
- `get_customer_most_spent_on_coffee(coffee_id)`: Retrieves the customer who spent the most on a specific coffee.

## SQL Queries

- **Get all orders for a specific coffee:**

  ```sql
  SELECT * FROM Orders
  WHERE coffee_id = ?;
  ```

- **Get distinct customers who ordered a specific coffee:**

  ```sql
  SELECT DISTINCT Customers.*
  FROM Customers
  JOIN Orders ON Customers.id = Orders.customer_id
  WHERE Orders.coffee_id = ?;
  ```

- **Get all orders for a specific customer:**

  ```sql
  SELECT * FROM Orders
  WHERE customer_id = ?;
  ```

- **Get distinct coffees ordered by a specific customer:**

  ```sql
  SELECT DISTINCT Coffees.*
  FROM Coffees
  JOIN Orders ON Coffees.id = Orders.coffee_id
  WHERE Orders.customer_id = ?;
  ```

- **Create a new order:**

  ```sql
  INSERT INTO Orders (customer_id, coffee_id, price)
  VALUES (?, ?, ?);
  ```

- **Get the number of orders for a specific coffee:**

  ```sql
  SELECT COUNT(*) FROM Orders
  WHERE coffee_id = ?;
  ```

- **Get the customer who spent the most on a specific coffee:**

  ```sql
  SELECT Customers.id, Customers.name, SUM(Orders.price) AS total_spent
  FROM Customers
  JOIN Orders ON Customers.id = Orders.customer_id
  WHERE Orders.coffee_id = ?
  GROUP BY Customers.id, Customers.name
  ORDER BY total_spent DESC
  LIMIT 1;
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

Feel free to customize it based on your specific needs or preferences!