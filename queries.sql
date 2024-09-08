-- Get all orders for a specific coffee
SELECT * FROM Orders
WHERE coffee_id = ?;

-- Get distinct customers who ordered a specific coffee
SELECT DISTINCT Customers.*
FROM Customers
JOIN Orders ON Customers.id = Orders.customer_id
WHERE Orders.coffee_id = ?;

-- Get all orders for a specific customer
SELECT * FROM Orders
WHERE customer_id = ?;

-- Get distinct coffees ordered by a specific customer
SELECT DISTINCT Coffees.*
FROM Coffees
JOIN Orders ON Coffees.id = Orders.coffee_id
WHERE Orders.customer_id = ?;

-- Create a new order
INSERT INTO Orders (customer_id, coffee_id, price)
VALUES (?, ?, ?);

-- Get the number of orders for a specific coffee
SELECT COUNT(*) FROM Orders
WHERE coffee_id = ?;

-- Get the customer who spent the most on a specific coffee
SELECT Customers.id, Customers.name, SUM(Orders.price) AS total_spent
FROM Customers
JOIN Orders ON Customers.id = Orders.customer_id
WHERE Orders.coffee_id = ?
GROUP BY Customers.id, Customers.name
ORDER BY total_spent DESC
LIMIT 1;
