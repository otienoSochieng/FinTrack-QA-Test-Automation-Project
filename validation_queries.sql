-- Sample DB validation queries for FinTrack
-- Verify transaction count increased after adding expense
SELECT COUNT(*) FROM transactions WHERE user_id = 1;

-- Verify balance calculation
SELECT (SELECT SUM(amount) FROM incomes WHERE user_id=1) - (SELECT SUM(amount) FROM expenses WHERE user_id=1) AS balance;
