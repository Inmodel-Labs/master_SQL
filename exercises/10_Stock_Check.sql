-- ==========================================
-- PAGE 10: STOCK CHECK (DEBUGGING CHALLENGE)
-- ==========================================

/*
  PROBLEM: Out of Stock Alert
  We need to find products with ZERO stock. The query below is returning everything 
  EXCEPT the ones with zero stock.

  DEBUGGER HINT: The developer used '!= 0' when they should have used '= 0'.
*/

-- TODO: Fix the broken query below.
SELECT * FROM products WHERE stock_quantity != 0;
