-- ==========================================
-- PAGE 26: HAVING CLAUSE
-- ==========================================

/*
  PROBLEM: Filtering Groups
  Find which category_ids contain more than 2 products.

  ANALYSIS: 
  - You cannot use 'WHERE' with aggregate functions. 
  - Use 'GROUP BY category_id' followed by 'HAVING COUNT(*) > 2'.
*/

-- TODO: Write your query below.
