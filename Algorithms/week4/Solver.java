import java.util.*;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Queue;

public class Solver{

    private final Queue<Board> boards;
    private int moves;
    private boolean isSolvable;

    // Create a search node
    private class SearchNode implements Comparable<SearchNode>{
        private Board board;
        private int moves;
        private SearchNode previous;
        private int cachedPriority = -1;

        SearchNode(Board board, int moves, SearchNode previous){
            this.board = board;
            this.moves = moves;
            this.previous = previous;
        }

        private int priority(){
            if (cachedPriority == -1){
                cachedPriority = moves + board.manhattan();
            }
            return cachedPriority;
        }

        @Override
        public int compareTo(SearchNode that){
            if (this.priority() < that.priority()){
                return -1;
            }
            if (this.priority() > that.priority()){
                return +1;
            }
            return 0;
        }
    }

    // find a solution to the intial board (using A*)
    public Solver(Board initial){
        boards = new Queue<Board>();

        // Check to see if in initial was right
        if (initial.isGoal()) {
            isSolvable = true;
            this.boards.enqueue(initial);
            return;
        }

        // If one of the twins is the goal, ours isn't solvable
        if (initial.twin().isGoal()) {
            isSolvable = false;
            return;
        }

        // Initialize the priority queue
        MinPQ<SearchNode> minPQ = new MinPQ<SearchNode>();
        MinPQ<SearchNode> minPQTwin = new MinPQ<SearchNode>();

        moves = 0;
        Board board = initial;
        Board boardTwin = initial.twin();
        SearchNode node = new SearchNode(board, 0, null);
        SearchNode nodeTwin = new SearchNode(boardTwin, 0, null);

        minPQ.insert(node);
        minPQTwin.insert(nodeTwin);

        while (moves < 100){
            node = minPQ.delMin();
            nodeTwin = minPQTwin.delMin();

            board = node.board;
            boardTwin = nodeTwin.board;

            // If the twin solves, we can't
            if (boardTwin.isGoal()) {
                isSolvable = false;
                return;
            }

            if (board.isGoal()){
                isSolvable = true;
                this.boards.enqueue(board);
                while (node.previous != null) {
                    node = node.previous;
                    this.boards.enqueue(node.board);
                }
                return;
            }
            node.moves++;
            nodeTwin.moves++;

            Iterable<Board> neighbors = board.neighbors();
            for (Board neighbor: neighbors) {
                if (node.previous != null && neighbor.equals(node.previous.board)){
                    continue;
                }
                SearchNode newNode = new SearchNode(neighbor, node.moves, node);
                minPQ.insert(newNode);
            }

            Iterable<Board> neighborTwin = boardTwin.neighbors();
            for (Board neighbor : neighborTwin){
                if (node.previous != null && neighbor.equals(node.previous.board)){
                    continue;
                }
                SearchNode newNode = new SearchNode(neighbor, nodeTwin.moves, nodeTwin);
                minPQTwin.insert(newNode);
            }
        }

    }

    // Is the initial board solvable?
    public boolean isSolvable(){
        return isSolvable;
    }

    // Min number of moves to solve initial board ; -1 if unsolveable
    public int moves(){
        if (isSolvable)
            return boards.size() -1;
        return -1;
    }

    // Sequence of boards in a shortest solution; null if unsolvable
    public Iterable<Board> solution(){
        if (isSolvable)
            return boards;
        return null;
    }

    // Solve a puzzle
    public static void main(String[] args){

        // Create initial board from file
        In in = new In(args[0]);
        int N = in.readInt();
        int[][] blocks = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                blocks[i][j] = in.readInt();
        Board initial = new Board(blocks);

        // Solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }

}
