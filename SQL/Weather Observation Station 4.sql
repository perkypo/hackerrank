/* Find the difference between the total number of CITY entries in the 
table and the number of distinct CITY entries in the table.*/

select count(CITY)-count(DISTINCT(CITY)) from STATION;