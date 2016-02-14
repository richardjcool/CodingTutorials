import java.util.Arrays;

public class Board{
    private int[][] board;
    private int N;
    /*
    Construct a board from an N-by-N array of blocks
    where blocks[i][j] = block in row i, column j
    */
    public Board(int[][] blocks)
    {
        if (blocks == null) throw new NullPointerException();
        N = blocks.length;
        board = new int[N][N];
        for (int i = 0; i<N; i++){
            for(int j = 0; j < N; j++){
                board[i][j] = blocks[i][j];
                }
            }
        }
    }

    // Size of board, N (board is NxN)
    public int dimension(){
        return board.length;
    }

    // Number of blocks out of place
    public int hamming(){
    int counter = 0;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            if ( board[i][j] != N*i+j+1 & board[i][j] != 0){
                counter++;
            }
        }
    }
    return counter;

    /*
        Sum of Manhatten distances between blocks and goal.
        Remember manhatten distance is the sum of the vertical
        and horizontal distance from the blocks to their goals).
    */
    public int manhatten(){

        int distance = 0;
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                distance += abs(board[i][j] / N - i) + abs(board[i][j] % N - j);
            }
        }
        return manhatten
    }

    // is this board the goal?
    public boolean isGoal(){
        return hamming() == 0; // only happens when at goal
    }

    // A Board that is obtain by exchanging any pair of blocks
    public Board twin() {
        Board twin = new Board(board);
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                if (board[i][j] != 0 && twin[i][j+1] !=0){
                    twin.swap(i,j,i,j+1);
                    return twin;
                }
            }
        }
    }

    private void swap(int i, int j, int it, int jt){
        if (it < 0 || it >= N || jt < 0 || jt >= N)
            throw new IllegalArugmentException();

        int holder = board[i][j];
        board[i][j] = board[it][jt];
        board[it][jt] = holder;
    }

    public boolean equals(Object y){
        if (y == this)
            return true;
        if (y == null)
            return false;
        if (y.getClass() != this.getClass())
            return false;

        //Cast
        Board that = (Board) y;
        for (int i = 0; i < N ; i++){
            for (int j = 0; j<N ; j++){
                if (that.board[i][j] != this.board[i][j])
                    return false;
            }
        }
        return true;
    }

    //Need to write a wrapper to find where the zero is.  We can code it
    //as the N*i+j value.
    private int findZero(){
        for (int i = 0; i < N; i++){
            for (int j = 0; j<N;j++){
                if (board[i][j] == 0)
                    return N*i+j;
            }
        }
    }


    // All neighboring boards
    public Iterable<Board> neighbors(){
        Stack<Board> boards = new Stack<Board>();
        Board neighbor = new Board(board);

        // Only do this if the zero isn't in the first row
        int zeroRow, zeroCol;
        int zeroLoc = findZero();
        zeroRow = zeroLoc / N;
        zeroCol = zeroLoc % N;

        if (zeroRow > 0){
            Board copy = new Board(board);
            copy.swap(zeroRow, zeroCol, zeroRow-1, zeroCol);
            boards.push(copy);
        }

        if (zeroRow < N-1){
            Board copy = new Board(board);
            copy.swap(zeroRow, zeroCol, zeroRow+1, zeroCol);
            boards.push(copy);
        }

        if (zeroCol > 0){
            Board copy = new Board(board);
            copy.swap(zeroRow, zeroCol, zeroRow, zeroCol-1);
            boards.push(copy);
        }

        if (zeroCol < N-1){
            Board copy = new Board(board);
            copy.swap(zeroRow, zeroCol, zeroRow, zeroCol+1);
            boards.push(copy);
        }

        return boards;
    }

    // String representation of this board
    public String toString(){
        StringBuilder s = new StringBuilder();
        s.append(N + "\n");
        for (int i = 0; i<N;i++){
            for (int j = 0; j<N; j++){
                s.append(String.format("%d ", tiles[i][j]));
            }
            s.append("\n");
        }
        return s.toString();
    }

}
