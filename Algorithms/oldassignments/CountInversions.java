/***********************************
*
*
* This program takes lines of input (typically piped from a text file) and 
* counts the number of inversions present using a Divide and Conquer approach.
*
*
*
*
*
***********************************/
import java.io.*;
import java.util.ArrayList;


public class CountInversions{

	public static void main(String[] args) throws IOException {
		
		String infile = args[0];
		
		//read file into stream 
		FileInputStream fstream = new FileInputStream(infile);
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
		
		String strLine;
		ArrayList<Integer> values = new ArrayList<>();
		
		
		//Read File Line by Line
		while ((strLine = br.readLine()) != null) {
			//Add the element to an array
			values.add(Integer.parseInt(strLine));			
		}
		
		int valueSize = values.size();
		for(int i = 0; i < valueSize; i++){
			System.out.println(values.get(i));
		}
		
	
	}
}