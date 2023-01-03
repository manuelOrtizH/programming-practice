/* Manuel Ortiz at 2022
Extracted from: https://leetcode.com/problems/fix-names-in-a-table/ */

SELECT user_id, CONCAT(UPPER(LEFT(name,1)), LOWER(SUBSTRING(name, 2, LENGTH(name)))) as name FROM Users
ORDER BY user_id

-- SELECT user_id, CONCAT(UPPER(LEFT(name,1)), LOWER(RIGHT(name, LENGTH(name)-1))) as name FROM Users
-- ORDER BY user_id