/* Write your T-SQL query statement below */
SELECT A.employee_id as employee_id, A.name as name, COUNT(B.reports_to) AS reports_count, ROUND(AVG(B.age*1.00), 0) AS average_age
FROM Employees A JOIN Employees B ON
A.employee_id = B.reports_to
GROUP BY A.employee_id, A.name
ORDER BY A.employee_id