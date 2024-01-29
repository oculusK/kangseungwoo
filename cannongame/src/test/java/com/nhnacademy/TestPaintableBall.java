package com.nhnacademy;

import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrowsExactly;

import java.awt.Color;

import org.junit.jupiter.api.Test;

public class TestPaintableBall {
    @Test
    void testPaintableBallConstructor() {
        int x = 0;
        int y = 100;
        int radius = 10;
        Color color = Color.BLUE;

        PaintableBall ball = new PaintableBall(x, y, radius, color);
        assertEquals(color, ball.getColor());
    }

    @Test
    void testDefaultConstructor() {
        int x = 0;
        int y = 100;
        int radius = 100;

        PaintableBall ball = new PaintableBall(x, y, radius);
        assertEquals(PaintableBall.DEFAULT_COLOR, ball.getColor());
    }

    @Test
    void testNullColor() {
        int x = 0;
        int y = 100;
        int radius = 100;

        assertThrowsExactly(IllegalArgumentException.class, () -> {
            new PaintableBall(x, y, radius, null);
        });
    }

    @Test
    void testPaint() {
        DummyGraphics g = new DummyGraphics();
        int x = 0;
        int y = 100;
        int radius = 100;
        Color originalColor = Color.RED;
        Color color = Color.BLUE;

        PaintableBall ball = new PaintableBall(x, y, radius, color);

        g.setColor(originalColor);
        ball.paint(g);

        assertEquals(x - radius, g.getFillOvalX());
        assertEquals(y - radius, g.getFillOvalY());
        assertEquals(2 * radius, g.getFillOvalWidth());
        assertEquals(2 * radius, g.getFillOvalHeight());
        assertEquals(originalColor, g.getColor());
    }
}
