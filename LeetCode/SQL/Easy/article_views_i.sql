/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/article-views-i/ */

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY 1 ASC

-- SELECT DISTINCT author_id AS id
-- FROM Views
-- WHERE author_id = viewer_id
-- GROUP BY article_id
