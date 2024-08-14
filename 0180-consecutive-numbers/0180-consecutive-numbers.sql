/* Write your T-SQL query statement below */
-- id = 1 and id = 2 and id = 3 이면서 i1.num = 10 and i2.num = 10 and i3.num = 10 이면 연속적으로 동일한 숫자를 세번 가진 것 
SELECT distinct 
    i1.num as ConsecutiveNums 
FROM 
    logs i1,
    logs i2,
    logs i3
WHERE 
    i1.id=i2.id+1 AND 
    i2.id=i3.id+1 AND 
    i1.num=i2.num AND 
    i2.num=i3.num