--link to problem: https://datalemur.com/questions/click-through-rate

SELECT app_id, 
  ROUND(100.00 * SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END)  / 
  SUM(CASE WHEN event_type = 'impression' THEN 1 ELSE 0 END), 2) AS ctr
FROM events
WHERE timestamp >= DATE '2022-01-01'
  AND timestamp < DATE '2023-01-01'
GROUP BY app_id;
