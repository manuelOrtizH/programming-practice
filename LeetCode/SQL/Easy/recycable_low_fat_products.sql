/* Manuel Ortiz at 2022
Extracted from: https://leetcode.com/problems/recyclable-and-low-fat-products/ */

SELECT product_id
FROM Products
WHERE low_fats = 'Y' and recyclable = 'Y'