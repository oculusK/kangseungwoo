package com.nhnacademy;

import java.util.LinkedList;
import java.util.List;

import javax.swing.JPanel;

import java.awt.Graphics;

/**
 * 월드를 정의한다.
 */
public class World extends JPanel {
    List<Ball> ballList = new LinkedList<>();

    public World() {
        super();
    }

    public void add(Ball ball) {
        if ((ball == null)
                || (ball.getX() - ball.getRadius() < 0)
                || (ball.getX() + ball.getRadius() > getWidth())
                || (ball.getY() - ball.getRadius() < 0)
                || (ball.getY() + ball.getRadius() > getHeight())) {
            throw new IllegalArgumentException("ball is null.");
        }

        ballList.add(ball);

    }

    public void remove(Ball ball) {
        ballList.remove(ball);
    }

    @Override
    public void remove(int index) {
        ballList.remove(index);
    }

    public int getCount() {
        return ballList.size();
    }

    public Ball get(int index) {
        return ballList.get(index);
    }

    @Override
    public void paint(Graphics g) {

        super.paint(g);

        for (Ball ball : ballList) {
            if (ball instanceof PaintableBall) {
                ((PaintableBall) ball).paint(g);
            }
        }

    }

}
