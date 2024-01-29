package com.nhnacademy;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrowsExactly;

import java.util.Random;

import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.RepetitionInfo;
import org.junit.jupiter.api.Test;

class TestBall {
    @Test
    void testBallConstructor() {
        final int x = 10;
        final int y = 20;
        final int radius = 30;

        Ball ball = new Ball(x, y, radius);

        assertEquals(x, ball.getX());
        assertEquals(y, ball.getY());
        assertEquals(radius, ball.getRadius());
    }

    @RepeatedTest(100)
    void testBallRepeatedConstructor(RepetitionInfo info) {
        Random random = new Random();
        final int x = random.nextInt();
        final int y = random.nextInt();
        final int radius = random.nextInt(Integer.MAX_VALUE);

        Ball ball = new Ball(x, y, radius);

        assertEquals(x, ball.getX());
        assertEquals(y, ball.getY());
        assertEquals(radius, ball.getRadius());
    }

    @Test
    void testMinusRadius() {
        final int x = 10;
        final int y = 20;
        final int radius = -30;

        assertThrowsExactly(IllegalArgumentException.class, () -> {
            new Ball(x, y, radius);
        });
    }
}
