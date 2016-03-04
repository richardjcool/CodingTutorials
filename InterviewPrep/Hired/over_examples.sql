/* Let's say we are lookng at data from a weight lifting competition.
Some types of analysis we can do include:
*/

SELECT
  /* Just return the basic columns (more for bookkeeping) */
  LiftID,
  LiftDate,
  LifPersonID,
  LiftWeight,

  /*ROW_NUMBER will list the number of the number of the row
    ordered by LiftID and will reset for each new combination of
    LiftDate, LiftPerson
  */
  ROW_NUMBER() OVER (PARTITION BY LiftDate, LiftPersonID
                     ORDER BY LiftID) AS LiftNumForToday
  
