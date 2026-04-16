-- ==========================================
-- PAGE 20: DATE FILTERING (DEBUGGING CHALLENGE)
-- ==========================================

/*
  PROBLEM: Time Traveler Error
  We are looking for orders placed on or after April 16, 2026. 
  The query below is failing with a data error.

  DEBUGGER HINT: In SQLite, dates must be enclosed in single quotes as strings.
*/

-- TODO: Fix the broken query below.
SELECT * FROM orders WHERE order_date >= 2026-04-16;
