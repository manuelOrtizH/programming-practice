/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/ */

SELECT DISTINCT actor_id, director_id
FROM ActorDirector A
GROUP BY actor_id, director_id
HAVING COUNT(A.timestamp) >= 3