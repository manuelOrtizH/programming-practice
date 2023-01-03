/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/employees-with-missing-information/ */

SELECT A.employee_id
FROM  
  (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
   UNION 
   SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id))
AS A
WHERE A.salary IS NULL OR A.name IS NULL
ORDER BY 1 ASC;


-- SELECT C.employee_id 
--     FROM 
--     (SELECT A.employee_id from Employees A
--     UNION
--     SELECT B.employee_id from Salaries B) AS C
-- WHERE C.employee_id NOT IN 
--     (SELECT D.employee_id 
--     FROM Employees D 
--     INNER JOIN Salaries E ON D.employee_id = E.employee_id)
-- ORDER BY 1 ASC;