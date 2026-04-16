-- E-commerce Sample Data (Expanded for 40 Exercises)

-- 1. Users
INSERT INTO users (username, email, is_premium, registration_date) VALUES 
('alice_sql', 'alice@example.com', 1, '2025-01-15'),
('bob_data', 'bob@example.com', 0, '2025-02-10'),
('charlie_query', 'charlie@example.com', 0, '2025-02-20'),
('dana_db', 'dana@example.com', 1, '2025-03-01'),
('eve_analyst', 'eve@example.com', 0, '2025-03-15'),
('frank_dev', 'frank@example.com', 1, '2025-03-20'),
('grace_sql', 'grace@example.com', 0, '2025-04-01'),
('hank_data', 'hank@example.com', 0, '2025-04-05'),
('ivy_db', 'ivy@example.com', 0, '2025-04-10'),
('jack_admin', 'jack@example.com', 1, '2025-04-12');

-- 2. Categories
INSERT INTO categories (name, description) VALUES 
('Electronics', 'Gadgets, devices, and accessories'),
('Books', 'Physical and digital collections'),
('Home & Kitchen', 'Appliances and decor'),
('Apparel', 'Clothing and footwear'),
('Sports', 'Equipment and activewear');

-- 3. Products
INSERT INTO products (name, category_id, price, stock_quantity) VALUES 
('Laptop Pro', 1, 1200.00, 15),
('Smartphone X', 1, 800.00, 30),
('SQL Performance Tuning', 2, 45.00, 100),
('Database Design Patterns', 2, 55.00, 50),
('Coffee Maker', 3, 85.00, 20),
('Wireless Mouse', 1, 25.00, 200),
('Premium Hoodie', 4, 60.00, 40),
('Running Shoes', 5, 120.00, 25),
('Yoga Mat', 5, 30.00, 60),
('Blender', 3, 40.00, 45),
('Gaming Keyboard', 1, 150.00, 10),
('The Coder''s Handbook', 2, 20.00, 500),
('Modern SQL', 2, 65.00, 80),
('Desk Lamp', 3, 35.00, 0),
('Water Bottle', 5, 15.00, 150);

-- 4. Employees (Hierarchy)
-- Jack (CEO)
INSERT INTO employees (first_name, last_name, job_title, manager_id, department, salary, hire_date) VALUES 
('Jack', 'Master', 'CEO', NULL, 'Executive', 200000, '2020-01-01');
-- Jack's reports
INSERT INTO employees (first_name, last_name, job_title, manager_id, department, salary, hire_date) VALUES 
('Sarah', 'Smith', 'CTO', 1, 'Engineering', 150000, '2020-02-01'),
('Mike', 'Jones', 'Sales Director', 1, 'Sales', 140000, '2020-03-01');
-- Sarah's reports
INSERT INTO employees (first_name, last_name, job_title, manager_id, department, salary, hire_date) VALUES 
('Tom', 'Brown', 'Senior Dev', 2, 'Engineering', 120000, '2021-01-10'),
('Anna', 'White', 'Dev', 4, 'Engineering', 90000, '2022-05-15'),
('Liam', 'Davis', 'Junior Dev', 4, 'Engineering', 70000, '2023-10-01');
-- Mike's reports
INSERT INTO employees (first_name, last_name, job_title, manager_id, department, salary, hire_date) VALUES 
('Emma', 'Wilson', 'Sales Rep', 3, 'Sales', 80000, '2021-06-20'),
('Noah', 'Garcia', 'Sales Rep', 3, 'Sales', 82000, '2022-01-15');

-- 5. Orders
INSERT INTO orders (user_id, status, total_amount, order_date) VALUES 
(1, 'delivered', 1245.00, '2026-03-01 10:00:00'),
(2, 'delivered', 800.00, '2026-03-05 14:30:00'),
(1, 'shipped', 25.00, '2026-04-10 09:15:00'),
(3, 'pending', 45.00, '2026-04-12 11:00:00'),
(4, 'delivered', 145.00, '2026-04-14 16:20:00'),
(5, 'cancelled', 60.00, '2026-04-15 10:05:00'),
(6, 'delivered', 150.00, '2026-04-15 15:45:00'),
(1, 'pending', 120.00, '2026-04-16 08:00:00'),
(9, 'shipped', 65.00, '2026-04-16 11:30:00'),
(4, 'delivered', 30.00, '2026-04-16 14:00:00');

-- 6. Order Items
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES 
(1, 1, 1, 1200.00), (1, 3, 1, 45.00),
(2, 2, 1, 800.00),
(3, 6, 1, 25.00),
(4, 3, 1, 45.00),
(5, 5, 1, 85.00), (5, 7, 1, 60.00),
(6, 7, 1, 60.00),
(7, 11, 1, 150.00),
(8, 8, 1, 120.00),
(9, 13, 1, 65.00),
(10, 9, 1, 30.00);

-- 7. Reviews
INSERT INTO reviews (product_id, user_id, rating, comment) VALUES 
(1, 1, 5, 'Best laptop ever!'),
(2, 2, 4, 'Great phone, but expensive.'),
(3, 1, 5, 'A must-read for SQL devs.'),
(3, 3, 2, 'Too technical for me.'),
(5, 4, 4, 'Makes good coffee.'),
(11, 6, 5, 'Mechanical keys feel amazing.'),
(13, 9, 3, 'Okay, but covers basics.'),
(1, 4, 5, 'Highly recommended for performance.'),
(7, 5, 1, 'Size was wrong, returning.'),
(15, 1, 4, 'Keeps water cold.');

-- 8. Coupons
INSERT INTO coupons (code, discount_percent, is_active) VALUES 
('WELCOME10', 10, 1),
('OFFER50', 50, 0),
('SQLMASTER', 15, 1);
