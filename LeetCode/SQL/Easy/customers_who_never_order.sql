/* Manuel Ortiz at 2022
Extracted from: https://leetcode.com/problems/customers-who-never-order/ */

SELECT A.name as 'Customers'
FROM Customers A
LEFT JOIN Orders B ON A.id = B.customerId
WHERE B.customerId is NULL