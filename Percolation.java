import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.StdIn;

public class Percolation {

	//Declare some stuff that we will want!
	private int count;
	private boolean[][] grid;
	private WeightedQuickUnionUF uf;
	private WeightedQuickUnionUF ufNoBot;


	//The main Percolation Structure
	public Percolation(int N)
	{

		count = N;
		//Throw an exception if N isn't positive and non-zero
		if (N <= 0) throw new IllegalArgumentException();

		//Create an NxN grid that is blocked (i.e. elements are 0)
		grid = new boolean[N][N];


		//Initialize the UF structure.
		//We let this be N^2+2 to allow for the top and bottom
		//virtual buckets
		uf = new WeightedQuickUnionUF(N*N+2);
		ufNoBot = new WeightedQuickUnionUF(N*N+1);
		
	}


	//Create a method to check for the range allowed for i and j
	private void checkIndexRange(int i, int j)
	{
		int N = count;
		if ( (i < 1) || (i > N) || (j < 1) || (j > N) ) throw new IndexOutOfBoundsException();
		
	}

	//Create a private method to go from i,j in the grid to location
	//along the 1d line.
	//For this, 0 = top, 101 = bottom.
	private int xy2oneD(int i, int j)
	{
		int N = count;
		return (i-1)*N+j;
	}

	//Open Site (row i, column j) if it is not open already
	public void open(int i, int j)
	{
		int N = count;
		//Check for exceptions
		checkIndexRange(i, j);

		//Only proceed if this is a blocked spot
		if ( isOpen(i,j) == false )
		{

			//Set the grid value to 1. Remember i, j are 1 indexed
			grid[i-1][j-1] = true;

			//Now make some connections around this point
			int gridval = xy2oneD(i,j);

			//First check above
			if (i > 1)
			{
				int aboveval = xy2oneD(i-1,j);
				if ( isOpen(i-1,j) ) 
				{
					uf.union(gridval, aboveval);
					ufNoBot.union(gridval, aboveval);
				}
			}
			else 
			{
				uf.union(gridval, 0); // top virtual
				ufNoBot.union(gridval, 0);
			}

			//Now below
			
			if (i < N)
			{
				int belowval = xy2oneD(i+1,j);
				if ( isOpen(i+1,j) ){
					uf.union(gridval, belowval);
					ufNoBot.union(gridval, belowval);
				}

			}
			else uf.union(gridval, N*N+1); // bottom virtual

			//Now left
			if (j > 1)
			{
				int leftval = xy2oneD(i,j-1);
				if ( isOpen(i, j-1) )
				{ 
					uf.union(gridval, leftval);
					ufNoBot.union(gridval, leftval);
				}
			}

			//Finally, right
			if (j < N)
			{
				int rightval = xy2oneD(i,j+1);
				if ( (isOpen(i, j+1) ) )
				{ 
					uf.union(gridval, rightval);
					ufNoBot.union(gridval, rightval);
				}
			}

		}
	}


	//This just looks at two elements (i1,j1) and (i2,j2) and checks to 
	//see if they are connected
	private boolean isConnected(int i1, int j1, int i2, int j2)
	{
		int grid1 = xy2oneD(i1,j1);
		int grid2 = xy2oneD(i2,j1);
		return uf.connected(grid1, grid2);
	}

	//Is site open?
	public boolean isOpen(int i, int j)
	{
		//Check values of i, j
		checkIndexRange(i,j);
		return (grid[i-1][j-1] == true);

	}

	//Is the site full?
	public boolean isFull(int i, int j)
	{
		/* For this we need a definition of full.  From the assignment, 
		a full site is an open site that can be connect to an open site in the top row.
		For us, this means that we need to check if isOpen and connected to 0 (top) */

		//Check values of i,j
		checkIndexRange(i,j);

		//Check to see if we're Open
		if (isOpen(i,j) == false) return false;

		int gridval = xy2oneD(i,j);
		return ufNoBot.connected(gridval, 0); //Only connected if it's connected, but not through bottom.
	}

	//Does the system percolate?
	public boolean percolates()
	{
		/* The system will percolate if the top virtual item
		connects to the bottom virtual item. The top item is item 0, and
		the bottom item is N*N+1 */
		int N = count;
		return uf.connected(0, N*N+1);

	}

	//Testing client
	public static void main(String[] args)
	{
		int N = 10;
		Percolation perc = new Percolation(N);
		
		for (int i = 1; i < N; i++)
			perc.open(i,1);

		System.out.println(perc.percolates());
	}
}	