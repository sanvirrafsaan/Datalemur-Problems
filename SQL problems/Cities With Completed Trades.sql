-- link to problem: https://datalemur.com/questions/completed-trades

SELECT city, COUNT(*) AS total_orders
FROM trades t
LEFT JOIN users u
  ON u.user_id = t.user_id
WHERE t.status = 'Completed'
GROUP BY u.city
ORDER BY total_orders DESC
LIMIT 3;
