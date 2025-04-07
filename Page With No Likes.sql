-- Link to Problem: https://datalemur.com/questions/sql-page-with-no-likes
SELECT p1.page_id
FROM pages p1
LEFT JOIN page_likes p2
ON p1.page_id = p2.page_id
WHERE p2.page_id IS NULL;
