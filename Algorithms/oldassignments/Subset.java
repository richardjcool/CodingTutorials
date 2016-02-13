/*********************
Inputs:
  - commandline integer k
  - sequence of N strings from standard input using StdIn.readString();
  - print out exactly k of them uniformly at random
*/

import edu.princeton.cs.algs4.StdIn;


public class Subset{

  public static void main(String[] args)
  {

    String inp;

    int k = Integer.parseInt(args[0]);
    RandomizedQueue<String> rq = new RandomizedQueue<String>();


    while (!StdIn.isEmpty()){
      inp = StdIn.readString();
      rq.enqueue(inp);
    }

    for (int i=0; i<k; i++){
      System.out.println(rq.dequeue());
    }

  }

}
