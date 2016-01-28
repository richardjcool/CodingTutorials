import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.StdIn;

public class Percolation{

 /* NOTES about the assignment:
    i,j are integers between 1 and N where (1,1) is the upper-left side.

 Ensure:
  1. Throw a java.lang.IndexOutofBoundsException if any argument of
   open()
   isOpen()
 isFull()
 is outside the prescribed range.  The constructor should throw a
 java.lang.IllegalArgumetnException if N <= 0.

 2. The constructor can run in n**2 time, all methods should take constant
 time plus a cosntant number of calls to the union-find methods:
 union()
 find()
 connected()
 count()
*/

 private int N;
 private WeightedQuickUnionUF uf;
 
 public Percolation(int N)
 {
  
  //Check that N is the positive non-zero integer
  if (N <= 0) throw new IllegalArgumentException();
  
  /*
  For now, let's index every element as it's own number.
  We can do some math to figure out the position of the surrounding
  elements. This will let us check for connection with a UnionFind 
  */
  
  int[][] grid = new int[N][N];
  for(int i =0; i < N; i++){
   for(int j = 0; j < N; j++){
    grid[i][j] = 0; // blocked
   }	
  }  
    
  uf = new WeightedQuickUnionUF(N*N+2);
 }	
 
 

 public void open(int i, int j)
 {
  
   /* 
   This routine will open element (i,j) if it's not already open.
   When we open (i,j) we probably want to do a union. Need to find the union code here
   */
	
	//We need to union i,j with the elements above, below, right, and left of it.
	
	int gridval = (i-1)*N + j; // This runs from 1 to N*(N-1)+N = N^2 and represents the value of the grid in the uf
	
	// Union with i-1 if i > 1)
	int aboveval;
	if (i > 1) {aboveval = (i-2)*N + j;}
	else {aboveval = 0;} // If i = 1, then link to the virtual top bucket
	System.out.println(gridval);
	System.out.println(aboveval);
	uf.union(gridval, aboveval);
  
  
 }

 public boolean isOpen(int i, int j)
 {
  //is site (row i, column j) open?
 
  return true;
  
 }

 public boolean isFull(int i, int j)
 {
 /*
 Is site (row i, column j) full?
 Remember that full means it is both open and connected to an
 open site in the top row
 */
 
  return true; 
 
 }

 public boolean percolates()
 {
  //Does the system percolate?
  return false;
 }

 public static void main(String[] args)
 {
	int N = StdIn.readInt();
	Percolation perc = new Percolation(N);
	perc.open(1,1);
  
  
 }
 

}
