/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/top-travellers/ */


SELECT A.name, IFNULL(SUM(B.distance),0) AS travelled_distance
FROM Users A
LEFT JOIN Rides B ON A.id = B.user_id
GROUP BY B.user_id
ORDER BY travelled_distance DESC, A.name ASC