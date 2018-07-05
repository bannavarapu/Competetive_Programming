import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.*;
import static org.junit.Assert.*;

public class Solution {

    public static boolean hasPalindromePermutation(String theString) {

        // check if any permutation of the input is a palindrome
        HashMap<Character,Integer>hm = new HashMap();
        
        if(theString=="")
        return true;
        int l= theString.length();
        for(int i=0;i<l;i++)
        {
            if(hm.containsKey(theString.charAt(i)))
            {
                int temp=hm.get(theString.charAt(i));
                temp++;
                hm.put(theString.charAt(i),temp);
            }
            else
            {
                 hm.put(theString.charAt(i),1);
            }
        }
        if(l%2==0)
        {
            boolean flag=true;
         for(int i=0;i<l;i++)
         {
             if((hm.get(theString.charAt(i))%2!=0))
             {
             flag=false;
             break;
             }
         }
         if(flag==true)
         return true;
         return false;
        }
        else
        {
            int count=0;
            for(Character c: hm.keySet())
            {
                // System.out.println(c+" "+hm.get(c));
                if(hm.get(c)%2!=0)
                count++;
            }
         if(count==1)
         return true;        
         return false;
        }
    }
    // tests

    @Test
    public void permutationWithOddNumberOfCharsTest() {
        final boolean result = hasPalindromePermutation("aabcbcd");
        assertTrue(result);
    }

    @Test
    public void permutationWithEvenNumberOfCharsTest() {
        final boolean result = hasPalindromePermutation("aabccbdd");
        assertTrue(result);
    }

    @Test
    public void noPermutationWithOddNumberOfChars() {
        final boolean result = hasPalindromePermutation("aabcd");
        assertFalse(result);
    }

    @Test
    public void noPermutationWithEvenNumberOfCharsTest() {
        final boolean result = hasPalindromePermutation("aabbcd");
        assertFalse(result);
    }

    @Test
    public void emptyStringTest() {
        final boolean result = hasPalindromePermutation("");
        assertTrue(result);
    }

    @Test
    public void oneCharacterStringTest() {
        final boolean result = hasPalindromePermutation("a");
        assertTrue(result);
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
