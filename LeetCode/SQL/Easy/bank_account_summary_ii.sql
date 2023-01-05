/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/bank-account-summary-ii/ */

SELECT U.name, SUM(T.amount) AS balance
FROM Users U
LEFT JOIN Transactions T ON U.account = T.account
GROUP BY T.account
HAVING balance > 10000