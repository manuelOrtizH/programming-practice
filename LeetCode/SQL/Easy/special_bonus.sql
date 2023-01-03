/* Manuel Ortiz at 2022
Extracted from: https://leetcode.com/problems/calculate-special-bonus/ */

SELECT employee_id, IF(MOD(employee_id,2) <> 0  AND name NOT LIKE "M%", salary, 0) AS bonus
FROM Employees
ORDER BY employee_id