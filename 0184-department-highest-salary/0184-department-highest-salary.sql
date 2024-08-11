/* Write your T-SQL query statement below */
-- SELECT Dt.name as Department, ey.name as Employee, salary as Salary
-- FROM Employee ey JOIN Department Dt ON ey.departmentId = Dt.id

SELECT Dt.name as Department, ey.name as Employee, salary as Salary
FROM Employee ey JOIN Department Dt ON ey.departmentId = Dt.id JOIN (
SELECT departmentId, MAX(salary) as max_salary
FROM Employee
GROUP BY departmentId ) max_ ON Dt.id = max_.departMentId AND salary = max_salary
