public class QuickFindUF
{
	private int[] id;
	
	//Set id of each object to itselt to initialize
	public QuickFindUF(int N)
	{
		id = new int[N];
		for (int i = 0; i < N; i++)
			id[i] = i;
		
	}
	
	//Check whether p and q are in the same component
	public boolean connected(int p, int q)
	{
		return id[p]== id[q];
	}
	
	//Union two entries p and q
	public void union(int p, int q)
	{
		int pid = id[p];
		int qid = id[q];
		for (int i = 0; i < N; i++)
			if (id[i] == pid) id[i] = qid;
	}
	
}