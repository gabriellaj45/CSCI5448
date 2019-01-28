public class Circle extends Shape {

	public Circle(double area) {
		super(area);
	}
	
	public void display() {
		System.out.printf("I am a circle with an area of %.1f\n", super.getArea());
	}

}
