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
            arrayOfChars[k-i]=temp1;
            arrayOfChars[i]=temp2;
        }
    }
    
    
    public static void reverse(char[] arrayOfChars,int i, int j){
        int a=i;
        int b=j;
        int c=(a+b)/2;
        for(;a<=c;a++)
        {
            char temp1=arrayOfChars[a];
            char temp2=arrayOfChars[b];
            arrayOfChars[b]=temp1;
            arrayOfChars[a]=temp2;
            b--;
        }
    }

    public static void reverseWords(char[] message) {

        // decode the message by reversing the words
        reverse(message);
        
        int spaces=0;
        int startingindex=0;
        int length=message.length;
        for(int i=0;i<length;i++)
        {
            
            if(i==length-1 || message[i]==' ')
            {
                if(i==length-1)
                reverse(message,startingindex,i);
                else
                reverse(message,startingindex,i-1);
                startingindex=i+1;
            }
        }

    }

    // tests

    @Test
    public void oneWordTest() {
        final char[] expected = "vault".toCharArray();
        final char[] actual = "vault".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void twoWordsTest() {
        final char[] expected = "cake thief".toCharArray();
        final char[] actual = "thief cake".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void threeWordsTest() {
        final char[] expected = "get another one".toCharArray();
        final char[] actual = "one another get".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void multipleWordsSameLengthTest() {
        final char[] expected = "the cat ate the rat".toCharArray();
        final char[] actual = "rat the ate cat the".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void multipleWordsDifferentLengthsTest() {
        final char[] expected = "chocolate bundt cake is yummy".toCharArray();
        final char[] actual = "yummy is cake bundt chocolate".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void emptyStringTest() {
        final char[] expected = "".toCharArray();
        final char[] actual = "".toCharArray();
        reverseWords(actual);
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
