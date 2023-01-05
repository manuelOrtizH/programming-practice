/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/market-analysis-i/ */

SELECT A.user_id AS buyer_id, A.join_date, 
IFNULL(COUNT(B.order_date), 0) AS orders_in_2019
FROM Users A 
LEFT JOIN Orders B ON (A.user_id = B.buyer_id AND YEAR(B.order_date) = '2019')
GROUP BY A.user_id;