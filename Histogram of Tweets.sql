-- Link to problem: https://datalemur.com/questions/sql-histogram-tweets

--Create a query for the tweet bucket.
WITH t1 AS (
SELECT COUNT(tweet_id) AS tweet_bucket, user_id 
FROM tweets 
WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31' 
GROUP BY user_id)

SELECT t1.tweet_bucket, COUNT(*) AS users_num 
FROM t1
GROUP BY t1.tweet_bucket;
