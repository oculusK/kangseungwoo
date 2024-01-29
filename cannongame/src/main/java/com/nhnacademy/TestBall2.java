package com.nhnacademy;

import java.util.Random;

public class TestBall2 {
    public static void main(String[] args) {
        Random random = new Random();

        for (int i = 0; i < 100; i++) {
            final int x = random.nextInt() * (random.nextInt(2) == 0 ? 1 : -1);
            final int y = random.nextInt() * (random.nextInt(2) == 0 ? 1 : -1);
            final int radius = random.nextInt() * (random.nextInt(2) == 0 ? 1 : -1);

            try {
                Ball ball = new Ball(x, y, radius);

                System.out.println("X : " + x + ", Y : " + y + ", R : " + radius);

                if (ball.getX() != x) {
                    System.out.println("Ball의 x좌표가 다릅니다.");
                    System.exit(1);
                }

                if (ball.getY() != y) {
                    System.out.println("Ball의 y좌표가 다릅니다.");
                    System.exit(1);
                }

                if (ball.getRadius() != radius) {
                    System.out.println("Ball의 Radius가 다릅니다.");
                    System.exit(1);
                }
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }

        System.out.println("정상적으로 완료 되었습니다.");
    }
}
