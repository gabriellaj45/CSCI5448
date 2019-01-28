public class Triangle extends Shape {

	public Triangle(double area) {
		super(area);
	}
	
	public void display() {
		System.out.printf("I am a triangle with an area of %.1f\n", super.getArea());
	}
	

}
