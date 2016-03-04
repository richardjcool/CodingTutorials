/* This is data from a weight lifting competition to practice window
functions.
*/

SELECT
  LiftID,
  LiftPersonID,
  LiftWEight,
  LiftDate,

  /* This will show the ROW NUMBER ordered by Lift ID, the Counter will
     reset with each new combination of LiftDate and LiftPerson ID
  */

  ROW_NUMBER() OVER (PARTITION BY LiftDate, LiftPersonID,
                    ORDER BY LiftID) AS LiftNumForToday,

  /* Now, I want the Sum of all the Weights Lifted in three formats:
     1.) The total weight lifted over the entire set
     2.) The total weight lifted on the date LiftDate
     3.) The total weight lifted on the date for a specific person
  */
  SUM(LiftWeight) OVER () as GrandTotal,
  SUM(LiftWeight) OVER (PARTITION BY LiftDate) as DailyWeight,
  SUM(LiftWeight) OVER (PARTITION BY LiftDate, LiftPersonID) as PersonDailyWeight,

  /* LAG and LEAD allow the current row to report entries from the previous
     and next entry respectively.
     Use LAG to return the weight from 1 row behind 1 ( in order of liftID ). Instead
     of returning NULL for missing data, return 0.
     Use LEAD to get the LiftWeight from 3 rows ahead. If no data return NULL
  */
  LAG(LiftWeight, 1, 0) OVER (ORDER BY LiftID) as prevLift,
  LEAD(LiftWeight, 3, NULL) OVER (ORDER BY LiftID) as nextLift,

  /* FIRST_VALUE and LAST_VALUE will return the specified column's first and
     last value in the result set.
  */
  FIRST_VALUE(LiftWeight) OVER (ORDER BY LiftDate) as FirstLift,
  LAST_VALUE(LiftWeight) OVER (ORDER BY LiftDate ROW BETWEEN
                               UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as LastLift,

  /* SUM using the ROWS BETWEEN will narrow the scope evaluated by the window
     function.   The function will begin and end where the ROWS BETWEEN specify
     The first SUM will add all the LiftWEight in all values up to and including
     the current row (CUMSUM)
     The second SUM will add the LiftWeight values in rows between the current
     row and the 3 rows before it
  */

  SUM(LiftWeight) OVER (ORDER BY LiftDate ROWS BETWEEN
                        UNBOUNDED PRECEDING AND CURRENT ROW) as CumSum
  SUM(LiftWeight) OVER (ORDER BY LiftDate ROWS BETWEEN
                        3 PRECEDING AND CURRENT ROW) as WeightLast4
  FROM dbo.Lifts;
  
