import Interfaces.CylinderInterface;

public class Cylinder extends Circle implements CylinderInterface {
    private float height;

    public Cylinder() {

    }

    public Cylinder(float height) {
        this.height = height;
    }

    public float getSideSquare() {
        float square = 0;
        //calculate cylinder's square here
        return square;
    }

    public float getVolume() {
        return super.getSquare()*height + super.getLength();
    }

    public float getPerim() {
        float perim = 0;
        //calculate cylinder's perimeter here
        return perim;
    }

    @Override
    public float getSquare() {
        return super.getSquare();
    }

    @Override
    public float getLength() {
        return super.getLength();
    }

    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
}
