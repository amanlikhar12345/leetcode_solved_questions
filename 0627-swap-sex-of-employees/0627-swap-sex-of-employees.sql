# Write your MySQL query statement bel
update Salary set sex= CASE sex
    WHEN "m" THEN "f"
    WHEN "f" THEN "m"

END;