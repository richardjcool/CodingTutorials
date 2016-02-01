/* This is an implementation of the double-ended queue or deque.
   It supports adding and removing items from either the front or the
   back of the data structure. */





import java.util.Iterator;
import java.util.NoSuchElementException;


public class Deque<Item> implements Iterable<Item>{

  /* Since the requirements for this assignment are constant worst case time
     We can't use array resizing. So we'll use a linked list. Let's set that up. */
  private Node<Item> first, last, head, tail;
  private int N = 0;

  private class Node<Item>
  {
    Item item;
    Node<Item> next;
    Node<Item> prev;
  }

  public Deque() // Construct an empty deque
  {
    head = new Node<Item>(); //This is like a "phantom" head tracer above first
    tail = new Node<Item>(); //This keeps track of where last would be.
    head.next = tail;
    tail.prev = head;
    N = 0;
  }

  public boolean isEmpty() // is the deque empty?
  {
    return N == 0;
  }

  public int size() // return the number of items on the deque
  {
    return N;
  }


  public void addFirst(Item item) // add the item to the front
  {
    if (item == null) throw new java.lang.NullPointerException();

    Node<Item> oldFirst = head.next;
    Node<Item> first = new Node<Item>();
    first.item = item;
    first.prev = head;
    first.next = oldFirst;

    //Update where the firsts are referenced from
    oldFirst.prev = first;
    head.next = first;


    N++;

  }

   public void addLast(Item item) // add the item to the end
  {
    if (item == null) throw new java.lang.NullPointerException();
    Node<Item> oldlast = tail.prev;
    Node<Item> last = new Node<Item>();
    last.item = item;
    last.next = tail;
    last.prev = oldlast;

    oldlast.next = last;
    tail.prev = last;
    N++;
  }

  public Item removeFirst() {
       if (isEmpty()) throw new NoSuchElementException("Deque underflow");
        Item item = head.next.item;
        head.next = head.next.next;
        head.next.prev = head;
        N--;
        return item;
  }



  public Item removeLast()
  {
    if (isEmpty()) throw new NoSuchElementException("Stack underflow");

    Item item = tail.prev.item;
    tail.prev = tail.prev.prev; // point to penultimate
    tail.prev.next = tail;
    N--;
    return item;
  }



  public Iterator<Item> iterator()
  { return new ListIterator(); }

  private class ListIterator implements Iterator<Item> {
    private Node<Item> current = first;

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
    System.out.println(dq.removeFirst());
  }


 }

}
