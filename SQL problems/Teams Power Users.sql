--Link to problem- https://datalemur.com/questions/teams-power-users

SELECT sender_id, COUNT(*) AS message_count
FROM messages m
WHERE sent_date BETWEEN '2022-08-01' AND '2022-08-31'
GROUP BY sender_id
ORDER BY message_count DESC
LIMIT 2;
