import java.util.*;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class FastCollinearPoints{

    private HashMap<Double, List<Point>> foundSeg = new HashMap<>();
    private int nSeg;
    private List<LineSegment> segments = new ArrayList<>();


    /* Check input for repeated values */
    private void checkDuplicates(Point[] points){
        int N = points.length;
        for (int i = 0; i < N; i++){
            for (int j = i+1; j < N ; j++){
                if (points[i] == null or points[j] == null){
                    throw new IllegalArgumentException();
                }
                if (points[i].compareTo(points[j]) == 0){
                    throw new IllegalArgumentException();
                }
            }
        }
    }

    /* Find all 4 or more colin points */
    public FastCollinearPoints(Point[] points){

        if (points == null) throw new IllegalArgumentException();

        //Check format of input
        ArrayList<LineSegment> foundSeg = new ArrayList<>();
        checkDuplicates(points);

        Point[] pnts = new Point[points.length];
        //Make a copy so we can do sorting wihout changing original order
        for (int i = 0; i < points.length ; i++)
            pnts[i] = points[i];


        for (Point nodePoint : points){

          Arrays.sort(pnts, nodePoint.slopeOrder());
          double slope = 0.0;
          double prevSlope = Double.NEGATIVE_INFINITY;
          ArrayList<Point> currentLine = new ArrayList<>();

          //Loop through the slopes (can start at 1, since 0 is itself)
          for (int i = 1; i < points.length; i++)
          {
            slope = nodePoint.slopeTo(pnts[i]);
            if (slope == prevSlope){
              currentLine.add(pnts[i]);
            } else {
              if (currentLine.size() >= 3){
                //We found 3 co-linear points with nodePoint, add them.
                currentLine.add(nodePoint);
                addSegment(currentLine, prevSlope);
              }
              currentLine.clear();
              currentLine.add(pnts[i]);
            }
            prevSlope = slope;
          }

          if (currentLine.size() >= 3){
            currentLine.add(nodePoint);
            addSegment(currentLine, slope);
          }
        }
    }

    private void addSegment(List<Point> Line, double slope){

        List<Point> endPoints = foundSeg.get(slope);
        Collections.sort(Line);

        Point startPoint = Line.get(0);
        Point endPoint = Line.get(Line.size() - 1);

        if (endPoints == null){
            endPoints = new ArrayList<>();
            endPoints.add(endPoint);
            foundSeg.put(slope, endPoints);
            segments.add(new LineSegment(startPoint, endPoint));
        } else {
            for (Point iEndPnt : endPoints){
                if (iEndPnt.compareTo(endPoint) == 0)  return;
            }
            endPoints.add(endPoint);
            segments.add(new LineSegment(startPoint, endPoint));
        }

    }



    /* number of segments found */
    public int numberOfSegments(){
        return segments.size();
    }

    /* the line Segments */
    public LineSegment[] segments(){
        return segments.toArray(new LineSegment[segments.size()]);
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
