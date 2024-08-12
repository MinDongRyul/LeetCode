/* Write your T-SQL query statement below */
-- SELECT 
--     cu.name as Customers
-- FROM 
--     Customers cu 
-- WHERE 
--     cu.id NOT IN (
--         SELECT customerId 
--         FROM Orders
--         )

select name as customers 
from Customers c left join Orders o on c.id=o.customerId 
where customerId is null
