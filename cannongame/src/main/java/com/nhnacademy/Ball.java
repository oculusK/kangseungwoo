package com.nhnacademy;

public class Ball {
    int x;
    int y;
    int radius;

    /**
     * 기본정보
     * 
     * @param x
     * @param y
     * @param radius
     */
    public Ball(int x, int y, int radius) {
        if (radius < 0) {
            throw new IllegalArgumentException("반지름은 0 또는 양수만 가능합니다.");
        }

        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getRadius() {
        return radius;
    }
}
