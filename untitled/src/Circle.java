import Interfaces.CircleInterface;

public class Circle implements CircleInterface {
    private float r;

    public Circle() {
    }

    public Circle(float r) {
        this.r = r;
    }

    public float getSquare() {
        float square = 0;
        //calculate circle's square here
        return square;
    }

    public float getLength() {
        float length = 0;
        //calculate circle's length here
        return length;
    }

    public float getR() {
        return r;
    }

    public void setR(float r) {
        this.r = r;
    }
}
