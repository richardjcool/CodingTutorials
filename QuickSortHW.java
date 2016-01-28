import java.util.Scanner;

public class QuickSortHW
{

	//The partition step
	public static int Partition(int[] A, int l, int r)
	{
		int p = A[l];
		int i = l + 1 ;
		
		
		for(int j = l+1; j < r; j++)
		{
			if (A[j] < p)
			{

				//Swap the values in A[j] and A[i]
				int itmp = A[i];
				int jtmp = A[j];
				A[i] = jtmp;
				A[j] = itmp;
				i++;
			}
		}
		//Swap the values of A[l] and A[i-1]
		int itmp = A[i-1];
		int ltmp = A[l];
		A[i-1] = ltmp;
		A[l] = itmp;
		return i-1;
	}

	public static int ChoosePivotLastElement(int[] A, int l, int r)
	{
		//For this case, always choose the last one
		return r-1;
	}

	public static int ChoosePivotFirstElement(int[] A, int l, int r)
	{
		//For this case, always choose the first one
		return l;
	}
	
	public static int ChoosePivotMedian(int[] A, int l, int r)
	{
		/*
		Notes from the assignment
		We need to find the median value of the first, last, and middle entry
		of A from l to r. 
		
		Namely, A[l], A[r-1], and A[n/2] but that only works for odd.  So probably want floor(n/2)
		*/
		
		int n = r - l ;
		if (n == 1) return l;
		if (n == 2) return l;
		
		int first = A[l];
		int last = A[r-1];
		int midindex = -1;
		if (n%2 == 1) midindex = l+(r-l)/2;
		if (n%2 == 0) midindex = l+(r-l-1)/2;
		int mid = A[midindex];
	
		
		int max = first;
		int min = first;
		
		int[] B = {first, mid, last};
		for(int i = 1; i < 3; i++)
		{
			int val = B[i];
			if (val < min) min = val;
			if (val > max) max = val;
		}	

		if (first != min && first != max) return l;
		if (last != min && last != max) return r-1;
		if (mid != min && mid != max) return midindex;
		return -1;
	}
	
	public static int QuickSort(int[] A, int l, int r, int ncomp)
	{
		int n = r - l;
		if (n == 1) return ncomp;		
		

		
		//int p = ChoosePivotFirstElement(A, l, r);
		int p = ChoosePivotMedian(A, l, r);
		//int p = ChoosePivotLastElement(A, l, r);
		
		
		//Swap the first element we are looking at with the pivot element
		int ltmp = A[l];
		int ptmp = A[p];
		A[l] = ptmp;
		A[p] = ltmp;
		
		int ipart = Partition(A, l, r);
		ncomp = ncomp + n - 1;	
		
		if ( (ipart) > l ) 
		{
			ncomp = QuickSort(A, l, ipart, ncomp);
		}
		
		if ( (ipart+1) < r ) 
		{
			ncomp = QuickSort(A, ipart+1, r, ncomp);		
		}
		return ncomp;
	}
		
	
	
	public static void main(String[] args){
		
		int N;
		int ncomp = 0;
		
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
			
		int[] array = new int[N];
		

		for(int i=0; i<N;i++)
		{
			array[i] = sc.nextInt();
		}
		
		
		ncomp = QuickSort(array, 0, N, ncomp);
		
		
		System.out.println("This required comparions : " + ncomp);
		
	
	
	}
	
	
	
	
	
	
}