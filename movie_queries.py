# Da’Vine Joy Randolph won an Oscar this year for her work in The Holdovers. 
# Write a query to determine the names and dates of birth of all people in the database whose name includes “Joy” somewhere in their name 
# it doesn’t matter where. 
# Use pattern-matching with an appropriate pattern. 
# The result of your query should be tuples of the form (name, date of birth).

problem4 = """
SELECT P.name, P.dob
FROM Person P
WHERE P.name LIKE '%Joy%'
"""

# The Holdovers is set in the Boston area. Another movie from the past decade that is also set here is Spotlight. 
# Write a single query that finds the runtimes of those two movies. The result of the query should be two tuples of the form (name, runtime).

problem5 = """
SELECT M.name, M.runtime
FROM Movie M
WHERE M.name = 'The Holdovers' OR M.name = 'Spotlight'
"""

# Robert Downey Jr. won a Best Supporting Actor Oscar this year for his work in Oppenheimer. 
# Write a query to find the names of all movies in our database in which he has acted. 
# Note: Downey’s name does not include a comma before the “Jr.”.

problem6 = """
SELECT M.name
FROM Movie M
WHERE  M.id IN (
				SELECT DISTINCT A.movie_id
				FROM Actor A
				WHERE A.actor_id IN (
										SELECT P.id
										FROM Person P
										WHERE P.name = 'Robert Downey Jr.'))
"""

# Casey Affleck was born in Massachusetts, and he won a Best Actor Oscar for his performance in the movie Manchester by the Sea. 
# Find the number of Oscar winners in our database who were born in Massachusetts. 
# You may assume that all such people have a place of birth that ends with “Massachusetts, USA”. 
# The result of your query should be a single number.

problem7 = """
SELECT DISTINCT COUNT(DISTINCT O.person_id)
FROM Oscar O
WHERE O.person_id IN (
										SELECT P.id
										FROM Person P
										WHERE P.pob LIKE '%Massachusetts, USA'
										)
"""

# Do movies with certain ratings tend to be more profitable? 
# For each movie rating that occurs in the 200 top-grossing movies (i.e., movies with an earnings rank of less than or equal to 200), 
# find the number of top-grossing movies with that rating, and the earnings rank of the most profitable movie with that rating. 
# The result of the query should be tuples of the form (rating, number of top grossers, earnings rank of most profitable movie).

problem8 = """
SELECT M.rating, COUNT(*), MIN(M.earnings_rank)
FROM Movie M
WHERE M.earnings_rank <= 200
GROUP BY M.rating    
"""

# Write a query to find the oldest animated movie(s) in the database, making use of the fact that all animated movies 
# have the letter N somewhere in the value of their genre attribute. 
# For example, The Lion King has a genre value of ‘VNCFL’, with the N indicating that it is animated. 
# If multiple animated movies are tied for being oldest, they should all be included. 
# The result of the query should be one or more tuples of the form (movie name, year).

problem9 = """
SELECT M.name, M.year
FROM Movie M
WHERE year = (SELECT MIN(M.year)
			  FROM Movie M
			  WHERE M.genre LIKE '%N%') AND M.genre LIKE '%N%'
 
"""

# Find the names of all people that have won at least 3 of the Oscars in the database. 
# The result of the query should be tuples of the form (name, number of Oscars). 
# Sort the results in descending order by the number of Oscars won. If multiple people are tied for number of Oscars, sort them in ascending order by name.

problem10 = """
SELECT P.name, COUNT(O.person_id) AS Oscars
FROM Oscar O, Person P
WHERE O.person_id = P.id
GROUP BY P.name
HAVING COUNT(O.person_id) >= 3
ORDER BY Oscars DESC
"""

# Write a query that summarizes the number of Oscars won by movies in the database that were released in 2023. 
# The result of the query should be tuples of the form (movie name, number of Oscars). 
# If a movie has won no awards, it should still appear in the table with a value of 0 for the number of Oscars. 
# You may assume that all movies from 2023 have a unique name.

problem11 = """
SELECT m.name, COUNT(o.type) AS number_of_oscars
FROM Movie m
LEFT JOIN Oscar o ON m.id = o.movie_id
WHERE m.year = 2023
GROUP BY m.name
ORDER BY number_of_oscars DESC, m.name; 
"""

# Write a query to determine the number of actors in the database who have not appeared 
# in any of the movies in the database from the last 10 years (i.e., 2014 or later). 
# The result of the query should be a single number.

problem12 = """
SELECT COUNT(DISTINCT A.actor_id)
FROM Actor A
WHERE A.actor_id NOT IN (SELECT A.actor_id
						 FROM Actor A, Movie M
						 WHERE A.movie_id=M.id AND M.year >= 2014)       
"""

# Write a query that determines, for each type of Oscar included in the database, the average runtime of movies associated with that Oscar. 
# The result of the query should be six tuples of the form (oscar type, average runtime).

problem13 = """
SELECT o.type, AVG(m.runtime)
FROM Movie m
JOIN Oscar o ON m.id = o.movie_id
GROUP BY o.type
ORDER BY o.type;
"""

# Write a single query to find both the oldest and youngest persons in the database. 
# If multiple people are tied for being either youngest or oldest, they should all be included. 
# The result of the query should be tuples of the form (name, date of birth).
 
problem14 = """
SELECT name, dob
FROM Person
WHERE dob = (SELECT MIN(dob) FROM Person)
OR dob = (SELECT MAX(dob) FROM Person);      
"""

# Timothee Chalamet starred in two of the most successful movies of the past year: Wonka and Dune: Part Two. He is in our database, but his dob and pob values are currently NULL. 
# Write a SQL command to add the facts that he was born on December 27, 1995 (i.e., '1995-12-27') in New York City (i.e., 'New York, New York, USA'). 
# This is the only question from this section that does not call for a SELECT command. You will need to figure out the correct type of SQL command to use.

problem15 = """
UPDATE Person 
SET dob = '1995-12-27', pob = 'New York, New York, USA'
WHERE name = 'Timothee Chalamet'         
"""
