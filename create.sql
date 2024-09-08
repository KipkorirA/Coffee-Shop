-- Create the Customers table
CREATE TABLE Customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL CHECK (length(name) BETWEEN 1 AND 15)
);

-- Create the Coffees table
CREATE TABLE Coffees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL CHECK (length(name) >= 3)
);

-- Create the Orders table
CREATE TABLE Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    coffee_id INTEGER,
    price REAL CHECK (price BETWEEN 1.0 AND 10.0),
    FOREIGN KEY (customer_id) REFERENCES Customers(id),
    FOREIGN KEY (coffee_id) REFERENCES Coffees(id)
);

-- Create indexes to optimize queries
CREATE INDEX idx_customer_id ON Orders(customer_id);
CREATE INDEX idx_coffee_id ON Orders(coffee_id);
