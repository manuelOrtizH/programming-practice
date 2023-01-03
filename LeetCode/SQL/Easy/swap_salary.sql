/* Manuel Ortiz at 2022 
Extracted from: https://leetcode.com/problems/swap-salary/ */

UPDATE Salary
SET sex = (CASE sex WHEN 'f' THEN 'm' ELSE 'f' END)
