/* Given two tables,
1. Candidate with ID, name
2. Vote with ID, candidateID

Give Query to give the name of the winning candidate
*/

SELECT
   name
from (
  SELECT
    candidate.name as name
    COUNT(1)
  FROM candidate JOIN vote ON candidate.id = vote.candidateid
  ORDER BY 2 DESC
  GROUP BY 1
) as c
LIMIT 1;

/* Calculating the median of a table positions */
SELECT x.price
FROM positions as x
  JOIN positions as y
GROUP BY x.price
HAVING SUM(SIGN(1-SIGN(y.price-x.price))) = (COUNT(1)+1)/2;

/* This works because if y-x is zero or > 0, then sum is just the sum
   of the elements less than it i.e. it's position in the row. If the position
   is N/2 (which is (N+1)/2 for integer math if N is odd), then we have reached
   the median
*/

/* Having is used so that we can compare aggreigates.  Otherwise, this would
   just return the prices. We choose which price by the one that has the right
   row count
*/
