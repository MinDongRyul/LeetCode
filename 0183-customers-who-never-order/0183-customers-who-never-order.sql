/* Write your T-SQL query statement below */
SELECT cu.name as Customers
FROM Customers cu 
WHERE cu.id NOT IN (SELECT customerId FROM Orders)
