package com.nhnacademy;

import java.awt.Color;
import java.awt.Graphics;

public class PaintableBall extends Ball {
    public static final Color DEFAULT_COLOR = Color.BLACK;
    Color color;

    // PaintableBall(int, int, int, Color)
    public PaintableBall(int x, int y, int radius, Color color) {
        super(x, y, radius);
        if (color == null) {
            throw new IllegalArgumentException();
        }
        this.color = color;
    }

    // PaintableBall(int, int, int) 파라미터 네임은 의미가 없다.
    public PaintableBall(int x, int y, int radius) {
        this(x, y, radius, DEFAULT_COLOR);
    }

    public Color getColor() {
        return color;
    }

    public void paint(Graphics g) {
        if (g == null) {
            throw new IllegalArgumentException();
        }

        Color previousColor = g.getColor();

        g.setColor(color);
        g.fillOval(getX() - getRadius(), getY() - getRadius(), 2 * getRadius(), 2 * getRadius());

        g.setColor(previousColor);
    }
}
