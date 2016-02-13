public class QuickFind
{
  private static int[] id, sz;

  public static void QuickFindUF(int N)
  {

    id = new int[N];
    sz = new int[N];
    for (int i = 0; i < N; i++)
    {
      id[i] = i;
      sz[i] = 1;
    }

  }

  public static void QFunion(int p, int q)
  {
    int pid = id[p];
    int qid = id[q];
    for (int i = 0; i < id.length; i++)
      if (id[i] == pid) id[i] = qid;
    }

  private static int root(int i)
  {
    while (i != id[i]) i = id[i];
    return i;
  }

  public static void WUFunion(int p, int q)
  {
    int i = root(p);
    int j = root(q);
    if (sz[i] < sz[j]) {id[i] = j; sz[j] += sz[i];}
    else {id[j] = i; sz[i] += sz[j];}

  }

  public static void main(String[] args)
  {
    QuickFindUF(10);
    WUFunion(1,4);
    WUFunion(6,0);
    WUFunion(3,6);
    WUFunion(8,2);
    WUFunion(3,7);
    WUFunion(7,5);
    WUFunion(2,1);
    WUFunion(6,1);
    WUFunion(9,4);

    for(int i = 0; i < id.length; i++)
      System.out.print(id[i] + " ");
    System.out.println("");

  }

}
