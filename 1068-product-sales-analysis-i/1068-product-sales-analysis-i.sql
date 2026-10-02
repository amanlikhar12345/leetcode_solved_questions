# Write your MySQL query statement below
select p.product_name ,year , price from Sales as s  join product p where p.product_id=s.product_id