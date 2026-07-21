-- Write your PostgreSQL query statement below
select person.firstName,person.lastname,Address.city,Address.state from Person left join Address on person.personid=Address.personid;