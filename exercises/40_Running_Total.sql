-- ==========================================
-- PAGE 40: RUNNING TOTAL (DEBUGGING CHALLENGE)
-- ==========================================

/*
  PROBLEM: The Window of Error
  The developer tried to calculate a running total but used 
  the wrong keyword for the window.

  DEBUGGER HINT: Window functions use the 'OVER' keyword, not 'WINDOW'.
*/

-- TODO: Fix the broken query below.
SELECT order_id, total_amount, SUM(total_amount) WINDOW(ORDER BY order_date) FROM orders;
