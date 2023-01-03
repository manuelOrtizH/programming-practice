/* Manuel Ortiz at 2022 
Extracted from: https://leetcode.com/problems/patients-with-a-condition/ */

SELECT * 
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'