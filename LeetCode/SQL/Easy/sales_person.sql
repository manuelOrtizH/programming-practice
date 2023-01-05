/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/sales-person/ */

SELECT SP.name
FROM SalesPerson SP
WHERE SP.sales_id NOT IN 
(
    SELECT O.sales_id
    FROM Company C
    RIGHT JOIN Orders O ON C.com_id = O.com_id
    WHERE C.name = 'RED'
);
