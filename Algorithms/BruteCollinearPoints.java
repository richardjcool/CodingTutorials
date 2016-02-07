/**
* This program examines 4 points at a time and checks wheather they all line
* on the same line segment. To check whether 4 points are collinear
* check to see that the slopes between p and q, p and r, and p and s are
* all equal.
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;


public class BruteCollinearPoints{

    private int nColin;
    private LineSegment[] segments;

    /* Check input for repeated values */
    private void checkDuplicates(Point[] points){
        int N = points.length;
        for (int i = 0; i < N; i++){
            for (int j = i+1; j < N ; j++){
                if (points[i].compareTo(points[j]) == 0){
                    throw new IllegalArgumentException();
                }
            }
        }
    }


    /* Check points for being the same and throw exception */
    private void isDupPoint(Point p, Point q){
        if (p.compareTo(q) == 0) throw new IllegalArgumentException();
    }

    /* Finds all line segments cont
    aining 4 points. */
    public BruteCollinearPoints(Point[] points)
    {
        checkDuplicates(points);
        if (points == null) throw new IllegalArgumentException();
        ArrayList<LineSegment> foundSeg = new ArrayList<>();


        int nColin = 0;
        int N = points.length;



        for (int i = 0; i < N; i++){
            for (int j = i+1; j < N; j++){
                for (int k = j+1; k < N; k++){
                    for (int l = k+1; l < N; l++){

                        //Check Slopes
                        double slope_ij = points[i].slopeTo(points[j]);
                        double slope_ik = points[i].slopeTo(points[k]);
                        double slope_il = points[i].slopeTo(points[l]);

                        if ( (slope_ij == slope_ik) &&
                             (slope_ij == slope_il))
                        {
                            Point[] subPoints = new Point[4];
                            subPoints[0] = points[i];
                            subPoints[1] = points[j];
                            subPoints[2] = points[k];
                            subPoints[3] = points[l];
                            Arrays.sort(subPoints);


                            foundSeg.add(new LineSegment(subPoints[0], subPoints[3]));
                            nColin++;
                           }


                    }
                }
            }

        }

        segments = foundSeg.toArray(new LineSegment[nColin]);
    }

    /* The number of line segments. */
    public int numberOfSegments(){
        return segments.length;
    }

    /* The line Segements.
    Should include each line sement containing 4 points exactly once
    If 4 points appear on a line segement then they should include
    either the line segment p>s or s>p (but not both) and you should
    not include subsegments p>r or p>q
    */
    public LineSegment[] segments(){
        return segments;
    }

    public static void main(String[] args){
        In in = new In(args[0]);
        int N = in.readInt();
        Point[] points = new Point[N];
        for (int i = 0; i < N; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
    }
        // print and draw the line segments
        BruteCollinearPoints collinear = new BruteCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
        }
    }
}
