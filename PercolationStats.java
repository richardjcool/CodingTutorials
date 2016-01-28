import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.StdIn;

public class PercolationStats {

	private int gridCount;
	private int trialCount;
	private double[] fracTrials;

	public PercolationStats(int N, int T)
	{
		gridCount = N;
		trialCount = T;

		if (N <= 0 || T <= 0) throw new IllegalArgumentException();


		fracTrials = new double[trialCount];
		
		for (int iTrial = 0; iTrial < trialCount; iTrial++){
		
			//Create a percolation object
			Percolation perc = new Percolation(gridCount);

			//We will set this to be false when we percolate
			boolean keepRunning = true;
			int openCount = 0; // This is the number of sites that we open

			while (keepRunning){

				//Grab random i and j
				int i = StdRandom.uniform(1, gridCount+1);
				int j = StdRandom.uniform(1, gridCount+1);

				//If this isn't open, then open it and increment count
				if (perc.isOpen(i,j) == false)
				{
					perc.open(i,j);
					openCount++;
				}

				//Check to see if we percolate
				if (perc.percolates())
					keepRunning = false;
					fracTrials[iTrial] = 1.0*openCount / gridCount / gridCount;
			}



		}



	}

	//Calculate the mean of the trial fractions
	public double mean()
	{
		return StdStats.mean(fracTrials);
	}


	public double stddev()
	{
		return StdStats.stddev(fracTrials);
	}	

	public double confidenceLo()
	{

		double meanVal = mean();
		double sigma = stddev();

		double conVal = meanVal - 1.96*sigma / Math.sqrt(trialCount);
		return conVal;
	}

	public double confidenceHi()
	{

		double meanVal = mean();
		double sigma = stddev();

		double conVal = meanVal + 1.96*sigma / Math.sqrt(trialCount);
		return conVal;
	}





	//Test Client 
	public static  void main(String[] args)
	{	

		int N = Integer.parseInt(args[0]);
		int T = Integer.parseInt(args[1]);	
		PercolationStats stats = new PercolationStats(N, T);
		System.out.println("mean                     = " + stats.mean());
		System.out.println("stddev                   = " + stats.stddev());
		System.out.println("95% Condifdence Interval = " + stats.confidenceLo() +", " + stats.confidenceHi());




	}



}