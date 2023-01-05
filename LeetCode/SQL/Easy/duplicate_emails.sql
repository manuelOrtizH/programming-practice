/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/duplicate-emails/ */

SELECT A.email AS Email
FROM Person A
GROUP BY A.email
HAVING COUNT(A.email) > 1

-- SELECT DISTINCT a.Email, a.id, b.id
-- FROM Person a 
-- INNER JOIN Person b ON (a.Email = b.Email)
-- WHERE a.Id <> b.Id

-- SELECT A.email
-- FROM Person A
-- LEFT JOIN Person B ON A.email = B.email
-- WHERE A.id < B.id