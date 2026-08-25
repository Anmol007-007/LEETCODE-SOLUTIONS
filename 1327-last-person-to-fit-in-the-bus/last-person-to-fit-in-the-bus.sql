with 
    new_table as 
    (select person_name,
    sum(weight) 
    over(order by turn) as sums from queue)
select 
    person_name 
    from new_table 
    where sums<=1000 
    order by sums desc 
    limit 1