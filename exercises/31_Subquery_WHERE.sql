-- ==========================================
-- PAGE 31: SUBQUERY IN WHERE
-- ==========================================

/*
  PROBLEM: Non-Purchasing Customers
  Identify all users who have never placed an order.

  ANALYSIS: 
  - Use a subquery to find all 'user_id' values in the 'orders' table.
  - Then, SELECT users WHERE their 'user_id' is NOT IN that list.
*/

-- TODO: Write your query below.
