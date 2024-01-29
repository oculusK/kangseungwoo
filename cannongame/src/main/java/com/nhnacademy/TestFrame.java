package com.nhnacademy;

import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;

public class TestFrame extends JFrame {
    PaintableBall ball;

    public TestFrame() {
        ball = new PaintableBall(200, 150, 50, Color.BLUE);
    }

    public static void main(String[] args) {
        TestFrame frame = new TestFrame();

        // 프레임 크기
        frame.setSize(400, 300);

        // true를 줘야 화면 킬수있음
        frame.setVisible(true);
        frame.setEnabled(true);
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);

        System.out.println("Call paint : " + System.currentTimeMillis());
        ball.paint(g);
    }
}
