public class Square extends Shape {

	public Square(double area) {
		super(area);
	}
	
	public void display() {
		System.out.printf("I am a square with an area of %.1f\n", super.getArea());
	}
}
