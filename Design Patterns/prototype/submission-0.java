interface Shape {
    Shape clone();
}

class Rectangle implements Shape {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int getWidth() {
        return this.width;
    }

    public int getHeight() {
        return this.height;
    }

    @Override
    public Shape clone() {
        // Write your code here
        Shape clonedShape = new Rectangle(this.width, this.height);
        return clonedShape;
    }
}

class Square implements Shape {
    private int length;

    public Square(int length) {
        this.length = length;
    }

    public int getLength() {
        return this.length;
    }

    @Override
    public Shape clone() {
        // Write your code here
        Shape clonedShape = new Square(this.length);
        return clonedShape;
    }
}

class Test {
    public List<Shape> cloneShapes(List<Shape> shapes) {
        // Write your code here
        List<Shape> clonedShapes = new ArrayList<Shape>();
        for (Shape shape : shapes) {
            Shape clonedShape = shape.clone();
            clonedShapes.add(clonedShape);
        }
        return clonedShapes;
    }
}
