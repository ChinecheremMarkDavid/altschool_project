
INSERT INTO Customers (customer_id, name, email, join_date) VALUES
(101, 'Sophia Rodriguez', 'sophia.rodriguez@gmail.com', '2023-11-05'),
(102, 'Ethan Carter', 'ethan.carter22@gmail.com', '2024-01-20'),
(103, 'Olivia Murphy', 'murphy.olivia@gmail.com', '2024-03-15'),
(104, 'Liam Patel', 'liam.patel.tech@gmail.com', '2024-05-10'),
(105, 'Ava Dubois', 'ava.dubois@gmail.com', '2024-07-28');

INSERT INTO products (product_id, product_name, category, price) VALUES
(1, 'Noise Cancelling Headphones', 'Audio', 249.99),
(2, 'Portable SSD 1TB', 'Storage', 79.50),
(3, 'Smart Watch Series 7', 'Wearables', 329.00),
(4, 'Premium Coffee Beans (1kg)', 'Food & Beverage', 19.99),
(5, 'Wireless Charging Pad', 'Accessories', 34.95),
(6, 'Smart Mug (12oz)', 'Accessories', 45.00);

INSERT INTO Orders (order_id, customer_id, product_id, quantity, order_date) VALUES
(1001, 101, 1, 1, '2023-11-08'),  
(1003, 103, 4, 3, '2024-03-17'),   
(1004, 101, 5, 2, '2024-04-01'),   
(1005, 104, 2, 1, '2024-05-11'),   
(1006, 102, 4, 1, '2024-06-05'),   
(1007, 105, 1, 1, '2024-07-30');



-- retrieve all orders made by a specific customer (Sophia Rodriguez, customer_id 101)
SELECT
    O.order_id,
    O.order_date,
    P.product_name,
    O.quantity
FROM
    Orders O
JOIN
    Customers C ON O.customer_id = C.customer_id
JOIN
    products P ON O.product_id = P.product_id
WHERE
    C.customer_id = 101;


-- get the total number of orders using count function  
SELECT
    COUNT(order_id) AS total_orders_count
FROM
    Orders;


-- Calculate the total revenue from all orders
SELECT
    SUM(P.price * O.quantity) AS total_revenue
FROM
    Orders O
JOIN
    products P ON O.product_id = P.product_id;


-- Use INNER JOIN to show full order details (Customer Name, Product Name)
SELECT
    O.order_id,
    C.name AS customer_name,
    P.product_name,
    O.quantity,
    P.price,
    (P.price * O.quantity) AS order_total
FROM
    Orders O
INNER JOIN
    Customers C ON O.customer_id = C.customer_id
INNER JOIN
    products P ON O.product_id = P.product_id
ORDER BY
    O.order_id;



-- Use LEFT JOIN to show all products and any related order (even if not sold)

SELECT
    P.product_name,
    P.price,
    O.order_id,
    O.order_date
FROM
    products P
LEFT JOIN
    Orders O ON P.product_id = O.product_id
ORDER BY
    P.product_id;