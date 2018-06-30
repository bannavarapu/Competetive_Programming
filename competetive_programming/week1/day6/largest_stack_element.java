import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.*;

import static org.junit.Assert.*;

public class Solution {

    // fill in the definitions for push(), pop(), and getMax()

    public static class MaxStack {
        ArrayList <Integer>al;
        int max;
        int count;
        MaxStack()
        {
            al= new ArrayList();
            count=0;
        }

        public void push(int item) {
            if(count==0)
            {
                max=item;
                al.add(item-max);
            }
            else
            {
                int temp=max-item;
                if(temp <0)
                {
                    max=item;
                }
                al.add(temp);
            }
            count++;
        }

        public int pop() {
            int temp=al.remove(count-1);
            if(temp<0)
            {
                int dummy= max;
                max=max+temp;
                temp=dummy;
            }
            else if(temp==0)
            {
                temp=max;   
            }
            else
            {
                temp=max-temp;
            }
            count--;
            return temp;
        }

        public int getMax() {
            return max;
        }
    }
    // tests

    @Test 
    public void maxStackTest() {
        final MaxStack s = new MaxStack();
        s.push(5);
        assertEquals("check max after 1st push", 5, s.getMax());
        s.push(4);
        s.push(7);
        s.push(7);
        s.push(8);
        assertEquals("check before 1st pop", 8, s.getMax());
        assertEquals("check pop #1", 8, s.pop());
        assertEquals("check max after 1st pop", 7, s.getMax());
        assertEquals("check pop #2", 7, s.pop());
        assertEquals("check max after 2nd pop", 7, s.getMax());
        assertEquals("check pop #3", 7, s.pop());
        assertEquals("check max after 3rd pop", 5, s.getMax());
        assertEquals("check pop #4", 4, s.pop());
        assertEquals("check max after 4th pop", 5, s.getMax());
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
