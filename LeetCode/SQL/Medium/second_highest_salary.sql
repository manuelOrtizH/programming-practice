/* Manuel Ortiz at 202 
Extracted from: https://leetcode.com/problems/second-highest-salary/ */

SELECT MAX(salary) SecondHighestSalary
FROM Employee A 
WHERE A.salary NOT IN (SELECT MAX(B.salary)
FROM Employee B )

-- SELECT
--     IFNULL(
--       (SELECT DISTINCT Salary
--        FROM Employee
--        ORDER BY Salary DESC
--         LIMIT 1 OFFSET 1),
--     NULL) AS SecondHighestSalary