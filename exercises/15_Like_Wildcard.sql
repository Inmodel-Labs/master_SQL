-- ==========================================
-- PAGE 15: LIKE WILDCARD (DEBUGGING CHALLENGE)
-- ==========================================

/*
  PROBLEM: The Searching Glitch
  The manager wants to find all products with 'SQL' in the name. 
  The query below is empty because the developer forgot the wildcards.

  DEBUGGER HINT: LIKE 'SQL' will only find rows where the name is EXACTLY 'SQL'. 
                 Use '%' to match characters before or after.
*/

-- TODO: Fix the broken query below.
SELECT * FROM products WHERE name LIKE 'SQL';
