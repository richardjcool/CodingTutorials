/*
    Given a set of N district points in the plane, find the (maximal)
    line sexment that connects a subset of 4 or more points.

*/

import java.util.Comparator;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class Point implements Comparable<Point> {

    private final int x; // x-coordinate of this point
    private final int y; // y-coordinate of this point

    /* Constructs a point (x,y) */
    public Point (int x, int y){
        this.x = x;
        this.y = y;
    }

    /* Draws the point */
    public void draw(){
        StdDraw.point(x,y);
    }

    /* Draws the line segment from this point to that point */
    public void drawTo(Point that){
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    /* String representation */
    public String toString(){
        return "(" + x + ", " + y + ")";
    }

    /* Compare two points by y-coordinate, breaking ties by x-coordinates.

    Formally, the invoking point (x0, y0) is less than the argument point
    (x1, y1) if and only if y0<y1 or if (y0=y1 and x0<x1).
    */
    public int compareTo(Point that){
        if ( (that.y == this.y) &&
             (that.x == this.x) ) {
            return 0;
        } else if (that.y==this.y) {
            if (this.x < that.x) return -1;
            else return 1;
        } else {
            if (this.y < that.y) return -1;
            else return 1;
        }

    }

    /* Find the slope between this point and that point.

    Treat : Horizontal as +0 slope,
            Vertical as positive infinity,
            Between line and itselt as negative infinity
    */
    public double slopeTo(Point that){
        if (this.x==that.x && this.y==that.y){
            return Double.NEGATIVE_INFINITY;
        } else if (this.y == that.y){
            return 0.0;
        } else if (this.x == that.x){
            return Double.POSITIVE_INFINITY;
        } else {
            return 1.0*(that.y-this.y)/(that.x-this.x);
        }
    }

    /* Compare two points by slopes they make with this point */
    public  Comparator<Point> slopeOrder(){
        return new Comparator<Point>(){
            public int compare(Point p, Point q) {
                double diff = slopeTo(p)-slopeTo(q);
                if (diff < 0) return -1;
                if (diff > 0) return 1;
                return 0;
            }
        };
    }

    /**
    * Unit tests the Point data type.
    */
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
        BruteCollinearPoints collinear = new BruteCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
    }


}
