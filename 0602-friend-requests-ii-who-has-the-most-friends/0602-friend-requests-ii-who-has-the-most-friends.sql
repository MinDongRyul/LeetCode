/* Write your T-SQL query statement below */
SELECT TOP 1 requester_id as id, COUNT(requester_id) as num
FROM (
SELECT * 
FROM RequestAccepted ra1 
UNION ALL
SELECT accepter_id, requester_id, accept_date
FROM RequestAccepted ra2
) ra_all
GROUP BY requester_id
ORDER BY num DESC