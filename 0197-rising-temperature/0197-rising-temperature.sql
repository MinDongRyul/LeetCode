/* Write your T-SQL query statement below */
SELECT w2.id AS ID
FROM Weather w1 LEFT OUTER JOIN Weather w2 
ON w1.recordDate = DATEADD(DAY, -1, w2.recordDate)
WHERE w1.temperature < w2.temperature