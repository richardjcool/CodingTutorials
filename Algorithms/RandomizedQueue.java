import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item>{
  private int N;
  private int first;
  private int last;
  private Item[] q;
  private int index;

  //  construct an empty randomized queue
  public RandomizedQueue()
  {
    q = (Item[]) new Object[2];       //Create the array with 2 elements
    N = 0;
    first = 0;
    last = 0;

  }

   //  is the queue empty?
  public boolean isEmpty()
  {
    return N == 0;
  }

  private void fullScan()
  {
    for (int i =0; i<q.length;i++){
      System.out.print(i + " ");
      System.out.println(q[i]);
    }
  }

  //Return the Number of Items on the Queue
  public int size()
  {
    return N;
  }

  private void resize(int max){
    Item[] temp = (Item[]) new Object[max];
    for (int i=0; i<N; i++){
      temp[i] = q[(first+i) % q.length];
    }
    q = temp;
    first = 0;
    last = N;
  }

  //  add the item
  public void enqueue(Item item)
  {
    if (N==q.length) resize(2*q.length);
    q[last++] = item;
    if (last == q.length) last = 0;
    N++;
  }
  //Remove and return a random item
  public Item dequeue()
  {
    if (isEmpty()) throw new NoSuchElementException("Queue underflow");
    index = StdRandom.uniform(0,N);

    Item item = q[index];
    q[index] = q[--last];
    q[last] = null;
    N--;
    if (first == q.length) first = 0;

    if (N > 0 && N == q.length/4) resize(q.length/2);
    return item;

  }

  //Return the least recently added to this queue
  public Item sample()
  {
    //This may have issues due to how I "pop" the null from the randomly
    //Chosen item to the end.
    if (isEmpty()) throw new NoSuchElementException("queue underflow");
    index = StdRandom.uniform(0,N);
    return q[index];
  }

  //Return an iterator that iterates over the items in *RANDOM* order
  public Iterator<Item> iterator()
  {
    return new ArrayRandomIterator();
  }

  //An iterator that randomly chooses the next item
  private class ArrayRandomIterator implements Iterator<Item>{
    private int i = 0;
    public boolean hasNext() {return N>0;};
    public void remove()
    {
      throw new UnsupportedOperationException();
    }

    public Item next(){
      if (!hasNext()) throw new NoSuchElementException();
      index = StdRandom.uniform(1, N);
      Item item = q[index];
      return item;
    }

  }


  public static void main(String[] args)
  {

    RandomizedQueue rq = new RandomizedQueue();

    for (int i = 0; i<10; i++)
      rq.enqueue(i);

    for (int i = 0; i<10; i++)
    {
        System.out.println(rq.dequeue());

    }

    for (int i = 0; i<100; i++)
      rq.enqueue(i);

    for (int i = 0; i<10; i++)
    {
      System.out.println(rq.dequeue());
    }


  }
}


/* Corner cases:

-- Throw a java.lang.NullPointerException if the client attempts to add a null item
-- throw a java.util.NoSuchElementException if the client attempts to sample or dequeue an item from an empty randomized queue
--  throw a java.lang.UnsupportedOperationException if the client calls the remove() method in the iterator;
-- throw a java.util.NoSuchElementException if the client calls the next() method in the iterator and there are no more items to return.

*/
