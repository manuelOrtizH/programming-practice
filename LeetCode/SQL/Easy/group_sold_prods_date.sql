/* Manuel Ortiz at 2022
Extracted from: https://leetcode.com/problems/group-sold-products-by-the-date/ */

SELECT sell_date, COUNT(DISTINCT product) as num_sold, 
GROUP_CONCAT(DISTINCT product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date, GROUP_CONCAT(DISTINCT product)