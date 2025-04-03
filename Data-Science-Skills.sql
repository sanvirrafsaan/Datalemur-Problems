--Link to question: https://datalemur.com/questions/matching-skills

SELECT c.candidate_id
FROM (
    SELECT candidate_id, COUNT(*) AS "count"
    FROM candidates
    WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
    GROUP BY candidate_id
) c
WHERE c.count = 3;
