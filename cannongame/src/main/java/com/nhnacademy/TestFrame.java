package com.nhnacademy;

import java.awt.Color;
import java.util.Random;

import javax.swing.JFrame;

public class TestFrame {

    public static void main(String[] args) {
        JFrame frame = new JFrame();

        // 프레임 크기
        frame.setSize(400, 300);

        World world = new World();

        world.setSize(400, 300);

        frame.add(world);

        Color[] colors = { Color.RED, Color.BLUE, Color.YELLOW, Color.MAGENTA, Color.GRAY, Color.GREEN };

        Random random = new Random();
        while (world.getCount() < 10) {
            int x = random.nextInt(400);
            int y = random.nextInt(300);
            int radius = 1 + random.nextInt(50);
            Color color = colors[random.nextInt(colors.length)];

            PaintableBall ball = new PaintableBall(x, y, radius, color);
            try {
                world.add(ball);
                System.out.println("X 좌표 : " + ball.getX() + ", Y좌표 : " + ball.getY() + ", 반지름 : " + ball.getRadius()
                        + ", 색깔 : " + ball.getColor());
            } catch (IllegalArgumentException e) {
                System.out.println("공이 공간을 벗어났습니다. : " + ball.getX() + ", " + ball.getY());
            }
        }

        // true를 줘야 화면 킬수있음
        frame.setVisible(true);
        frame.setEnabled(true);
    }
}
