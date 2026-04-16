-- ==========================================
-- PAGE 30: SELF JOIN (DEBUGGING CHALLENGE)
-- ==========================================

/*
  PROBLEM: The Alias Collision
  The developer tried to join the employees table to itself but got an 
  "ambiguous column" error.

  DEBUGGER HINT: When joining a table to itself, you MUST use different 
                 aliases (e.g., 'e' and 'm') to distinguish between the 
                 employee and their manager.
*/

-- TODO: Fix the broken query below.
SELECT first_name, first_name FROM employees JOIN employees ON manager_id = employee_id;
