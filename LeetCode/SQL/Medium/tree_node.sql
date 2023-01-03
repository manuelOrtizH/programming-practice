/* Manuel Ortiz at 2023 
Extracted from: https://leetcode.com/problems/tree-node/ */


SELECT A.id, 
(CASE
    WHEN A.p_id IS null THEN 'Root'
    WHEN A.id IN (SELECT B.p_id FROM Tree B) THEN 'Inner'
    ELSE 'Leaf' END
) as type
FROM Tree A

-- SELECT DISTINCT A.id, 
-- (CASE
--     WHEN A.p_id IS NULL THEN 'Root'
--     WHEN A.p_id IS NOT NULL AND B.p_id IS NOT NULL THEN 'Inner'
--     WHEN A.p_id IS NOT NULL AND B.p_id IS NULL THEN 'Leaf'
--     END
-- ) as type
-- FROM Tree A LEFT JOIN Tree B ON A.id = B.p_id