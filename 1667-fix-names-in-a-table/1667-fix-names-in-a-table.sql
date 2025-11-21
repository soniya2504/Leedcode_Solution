# Write your MySQL query statement below
SELECT
    user_id,
    -- Concatenate the uppercase first letter with the lowercase remainder of the name.
    -- SUBSTRING(name, 1, 1) extracts the first character.
    -- SUBSTRING(name, 2) extracts the string starting from the second character.
    CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM
    Users
-- The result table should be ordered by user_id.
ORDER BY
    user_id;