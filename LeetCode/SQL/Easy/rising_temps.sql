/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/rising-temperature/ */

SELECT A.id AS id
FROM Weather A
INNER JOIN Weather B ON TO_DAYS(A.recordDate) = TO_DAYS(B.recordDate) + 1
WHERE A.temperature > B.temperature;