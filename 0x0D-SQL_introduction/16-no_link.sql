-- Lists all records in the table second_table of the database hbtn_0c_0
-- Having a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
