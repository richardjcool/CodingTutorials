/* This is an implementation of the double-ended queue or deque.
   It supports adding and removing items from either the front or the
   back of the data structure. */





import java.util.Iterator;
import java.util.NoSuchElementException;


public class Deque<Item> implements Iterable<Item>{

  /* Since the requirements for this assignment are constant worst case time
     We can't use array resizing. So we'll use a linked list. Let's set that up. */
  private Node first, last;
  private int N = 0;

  private class Node
  {
    Item item;
    Node next;
  }

  public Deque() // Construct an empty deque
  {
    first = null;
    last = null;
    N = 0;
  }

  public boolean isEmpty() // is the deque empty?
  {
    return first == null;
  }

  public int size() // return the number of items on the deque
  {
    return N;
  }


  public void addFirst(Item item) // add the item to the front
  {
    if (item == null) throw new java.lang.NullPointerException();
    boolean wasEmpty;
    wasEmpty = isEmpty();
    Node oldfirst = first;
    first = new Node();
    first.item = item;
    first.next = oldfirst;

    if (wasEmpty) last = first;


    N++;

  }

   public void addLast(Item item) // add the item to the end
  {
    if (item == null) throw new java.lang.NullPointerException();
    Node oldlast = last;
    last = new Node();
    last.item = item;
    last.next = null;

    if (isEmpty()) first = last;
    else oldlast.next = last;

    N++;
  }


  public Item removeFirst() // remove and return the item from the front
  {
    if (isEmpty()) throw new NoSuchElementException("Stack underflow");
    Item item = first.item;
    first = first.next;
    N--;
    if (isEmpty()) last = null;
    return item;

  }

  public Item removeLast() // Remove and return the item from the end
  {
    if (isEmpty()) throw new NoSuchElementException("Stack underflow");

    Node oldLast = last;

    if (first == last){
      first = null;
      last = null;
    } else if (first != null){
        Node newLast = findSecondtoLast();
        newLast.next = null;
        last = newLast;
    } else{
      last = null;
    }
    N--;

    if (oldLast != null){
      return oldLast.item;
    } else{
      return first.item;
    }
  }

  private Node findSecondtoLast()
  {

    Node newLast = first;
    //Walk through elements until the next element is the last element
    while (newLast.next != null && newLast.next != last){
      newLast = newLast.next;
    }

    return newLast;
  }



  public Iterator<Item> iterator()
  { return new ListIterator(); }

  private class ListIterator implements Iterator<Item> {
    private Node current = first;

    public boolean hasNext() { return current != null; }
    public void remove()
    {
      throw new java.lang.UnsupportedOperationException();
    }

    public Item next() {
      if (!hasNext()) throw new  java.util.NoSuchElementException();
      Item item = current.item;
      current = current.next;
      return item;
    }

  }


  public static void main(String[] args) // unit testing
 {

  Deque dq = new Deque();
  for (int i = 1; i<10;i++)
    dq.addFirst(i);

  while(dq.isEmpty()==false)
  {
    System.out.println(dq.removeLast());
  }

  for (int i = 1; i<300; i++)
    dq.addLast(i);

  while(dq.isEmpty() == false)
  {
    System.out.println(dq.removeFirst() + " " + dq.size());
  }


 }

}
