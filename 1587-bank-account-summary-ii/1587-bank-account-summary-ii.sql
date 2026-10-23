# Write your MySQL query statement below

select u.name ,t.balance from Users u join (select account,sum(amount) as balance from Transactions group by account having sum(amount)>10000 ) t on t.account=u.account;