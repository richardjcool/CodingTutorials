/***************
* This program wil take three positive integers as command line arguements
* and print true if any one of them is greater than the sum of the others
****************/
public class isGreaterSum {
	public static void main(String[] args) {
		int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[1]);
		int c = Integer.parseInt(args[2]);
		
		boolean isGreater = ( (a > b + c) || (b > a + c) || (c > a + b) );
		System.out.println(isGreater);
			
	}
}