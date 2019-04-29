DELETE FROM Person
WHERE Id NOT IN (
    SELECT p.Id FROM (
        SELECT MIN(Id) as Id FROM Person GROUP BY Email
    ) as p 
)
