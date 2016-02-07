import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class FastCollinearPoints{


    private int nSeg;
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

    /* Find all 4 or more colin points */
    public FastCollinearPoints(Point[] points){

        Point[] sortedArray = new Point[points.length];
        ArrayList<Point> usedPoints = new ArrayList<>();

        nSeg = 0;



        // auxarray is there so sorting doesn't screw up our indexing
        for (int i = 0; i < points.length; i++){
            sortedArray[i] = points[i];
        }

        ArrayList<LineSegment> foundSeg = new ArrayList<>();
        if (points == null) throw new IllegalArgumentException();
        checkDuplicates(points);

        /* Set each p as origin */
        for (int i = 0; i < points.length; i++){

            Arrays.sort(sortedArray, points[i].slopeOrder());

            /*Now, loop through and check to see if i-1, i, and i+1 all have
            the same slope. If yes, they are colinear */
            double slope_j, slope_plus, slope_minus;

            for (int j = 1; j < points.length -1; j++){

                    //If this point was utilized in a segment, drop now

                    slope_j = points[i].slopeTo(sortedArray[j]);
                    slope_plus = points[i].slopeTo(sortedArray[j+1]);
                    slope_minus = points[i].slopeTo(sortedArray[j-1]);

                    boolean allUsed;
                    allUsed = (usedPoints.contains(sortedArray[j]) &&
                               usedPoints.contains(sortedArray[j-1]) &&
                               usedPoints.contains(sortedArray[j+1]));

                    if (slope_j == slope_plus &&
                        slope_j == slope_minus && allUsed == false){

                        //We have a pattern. We don't have to search backward
                        //Since we're incrementing that way, but lets check higher
                        int hi = 2;
                        boolean goFlag = true;
                        while (j+hi < points.length && goFlag == true){
                            if (points[i].slopeTo(sortedArray[j+hi]) ==
                                points[i].slopeTo(sortedArray[j])){
                                    hi++;
                                } else {
                                    goFlag = false;
                                }
                        }

                        Point[] subPoint = new Point[hi+2];
                        subPoint[0] = points[i];
                        usedPoints.add(subPoint[0]);
                        for (int k = -1; k < hi; k++){
                            subPoint[k+2] = sortedArray[j + k];
                            usedPoints.add(subPoint[k+2]);
                        }
                        Arrays.sort(subPoint);
                        foundSeg.add(new LineSegment(subPoint[0], subPoint[hi+1]));
                        nSeg++;
                    }
           }

        }
        segments = foundSeg.toArray(new LineSegment[nSeg]);
    }

    /* number of segments found */
    public int numberOfSegments(){
        return segments.length;
    }

    /* the line Segments */
    public LineSegment[] segments(){
        return segments;
    }

    public static void main(String[] args) {
        // read the N points from a file
    In in = new In(args[0]);
    int N = in.readInt();
    Point[] points = new Point[N];
    for (int i = 0; i < N; i++) {
        int x = in.readInt();
        int y = in.readInt();
        points[i] = new Point(x, y);
    }

    // draw the points
  StdDraw.show(0);
  StdDraw.setXscale(0, 32768);
  StdDraw.setYscale(0, 32768);
  for (Point p : points) {
      p.draw();
  }
  StdDraw.show();

    // print and draw the line segments
    FastCollinearPoints collinear = new FastCollinearPoints(points);
    StdOut.println(collinear.numberOfSegments());
    for (LineSegment segment : collinear.segments()) {
        StdOut.println(segment);
        segment.draw();
    }
    }
}
