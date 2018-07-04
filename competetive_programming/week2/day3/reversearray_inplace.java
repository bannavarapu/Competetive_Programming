import java.util.Arrays;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static void reverse(char[] arrayOfChars) {

        int j = arrayOfChars.length;
        int k=j-1;
        for(int i=0;i<j/2;i++)
        {
            char temp1=arrayOfChars[i];
            char temp2=arrayOfChars[k-i];
            // System.out.println(temp1+" "+temp2);
            arrayOfChars[k-i]=temp1;
            arrayOfChars[i]=temp2;
        }
    }

    // tests

    @Test
    public void emptyStringTest() {
        final char[] expected = "".toCharArray();
        final char[] actual = "".toCharArray();
        reverse(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void singleCharacterStringTest() {
        final char[] expected = "A".toCharArray();
        final char[] actual = "A".toCharArray();
        reverse(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void longerStringTest() {
        final char[] expected = "EDCBA".toCharArray();
        final char[] actual = "ABCDE".toCharArray();
        reverse(actual);
        assertArrayEquals(expected, actual);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}
