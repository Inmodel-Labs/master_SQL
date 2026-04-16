-- ==========================================
-- PAGE 05: LIMIT RESULTS (DEBUGGING CHALLENGE)
-- ==========================================

/*
  PROBLEM: The Broken Sample
  One of our developers tried to get the 5 most expensive products, 
  but the query is returning the 5 CHEAPEST instead.

  ANALYSIS: 
  - To get the MOST expensive, we need to sort in descending order.
  - The developer used 'ASC' or forgot to specify.

  DEBUGGER HINT: Fix the ORDER BY clause to get the top 5 highest prices.
*/

-- TODO: Fix the broken query below.
SELECT * FROM products ORDER BY price ASC LIMIT 5;
