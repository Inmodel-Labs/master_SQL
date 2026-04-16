-- ==========================================
-- PAGE 35: CASE BASICS (DEBUGGING CHALLENGE)
-- ==========================================

/*
  PROBLEM: The Incomplete Logic
  The developer started a CASE statement but it's failing because 
  it's missing the final piece.

  DEBUGGER HINT: Every CASE expression must conclude with the 'END' keyword.
*/

-- TODO: Fix the broken query below.
SELECT username, CASE WHEN is_premium = 1 THEN 'Premium' ELSE 'Standard' FROM users;
