/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/ */

SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM Visits A 
LEFT JOIN Transactions B ON A.visit_id = B.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id