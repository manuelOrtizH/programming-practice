/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/sales-analysis-iii/ */

SELECT A.product_id, A.product_name
FROM Product A
LEFT JOIN Sales B ON A.product_id = B.product_id
GROUP BY A.product_id
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'

-- SELECT A.product_id, A.product_name
-- FROM Product A
-- WHERE A.product_id IN 
-- (SELECT B.product_id
-- FROM Sales B
-- GROUP BY B.product_id
-- HAVING MIN(B.sale_date) >= '2019-01-01' AND MAX(B.sale_date) <= '2019-03-31')