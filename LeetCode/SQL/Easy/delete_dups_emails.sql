/* Manuel Ortiz at 2022
Extracted from: https://leetcode.com/problems/delete-duplicate-emails/ */

DELETE B FROM Person A
INNER JOIN Person B ON A.email = B.email
WHERE A.id < B.id



-- DELETE B FROM Person A, Person B
-- WHERE A.email = B.email AND B.id > A.id