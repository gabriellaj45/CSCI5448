import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		// create a collection of shapes, list of type Shape
		List <Shape> listOfShapes = new ArrayList<Shape>();
		
		Circle c = new Circle(2);
		Circle c1 = new Circle(4);
		Circle c2 = new Circle(6);
		Circle c3 = new Circle(8);
		Square s = new Square(5);
		Square s1 = new Square(10);
		Square s2 = new Square(15);
		Square s3 = new Square(20);
		Triangle t = new Triangle(3);
		Triangle t1 = new Triangle(6);
		Triangle t2 = new Triangle(9);
		Triangle t3 = new Triangle(12);
		
		listOfShapes.add(c);
		listOfShapes.add(c1);
		listOfShapes.add(c2);
		listOfShapes.add(c3);
		listOfShapes.add(s);
		listOfShapes.add(s1);
		listOfShapes.add(s2);
		listOfShapes.add(s3);
		listOfShapes.add(t);
		listOfShapes.add(t1);
		listOfShapes.add(t2);
		listOfShapes.add(t3);
		Collections.sort(listOfShapes, new Comparator<Shape>() {
	        @Override
	        public int compare(Shape o1, Shape o2) {
	            return Double.compare(o1.getArea(), o2.getArea());
	        }
	    });
		
		System.out.println("There are " + listOfShapes.size() + " shapes in this \"database\"");
		
		for(Shape shape: listOfShapes){ 
			shape.display();
		}
	}

}
