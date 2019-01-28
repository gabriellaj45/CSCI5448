
public abstract class Shape {

	private double doubleArea;
	
	public Shape(double area) {
		this.doubleArea = area;
	}
	
	public double getArea() {
		return doubleArea;
	}
	
	public void setArea(double area) {
		this.doubleArea = area;
	}
	
	public abstract void display();
}
