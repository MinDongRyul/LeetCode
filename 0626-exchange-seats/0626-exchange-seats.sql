/* Write your T-SQL query statement below */
SELECT id, 
    CASE WHEN id % 2 <> 0 THEN LEAD(student,1,student)OVER(ORDER BY id)
         WHEN id % 2 = 0 THEN LAG(student)OVER(ORDER BY id)
    END AS student
FROM Seat;