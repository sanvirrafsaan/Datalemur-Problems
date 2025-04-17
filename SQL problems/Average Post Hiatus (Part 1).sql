--Link to problem: https://datalemur.com/questions/sql-average-post-hiatus-1

SELECT user_id, EXTRACT(DAY from (MAX(post_date) - MIN(post_date))) AS "days_between"
FROM posts
WHERE EXTRACT(YEAR from post_date) = 2021 --YEAR(post_date) = 2021 in mysql
GROUP BY user_id 
HAVING COUNT(user_id) >= 2
