-- ==========================================
-- PAGE 25: GROUP BY BASICS (DEBUGGING CHALLENGE)
-- ==========================================

/*
  PROBLEM: The Non-Aggregated Column Error
  The query below is failing because the developer tried to select 
  'name' while grouping by 'category_id'.

  DEBUGGER HINT: When using GROUP BY, every column in the SELECT list must 
                 either be in the GROUP BY clause or have an aggregate 
                 function (like COUNT, SUM) applied to it.
*/

-- TODO: Fix the broken query below.
SELECT name, category_id, COUNT(*) FROM products GROUP BY category_id;
