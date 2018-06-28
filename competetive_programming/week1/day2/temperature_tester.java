public class Solution {

    static class TempTracker {

        // fill in the TempTracker class methods below
        int sum;
        double mean;
        int mode;
        int min;
        int max;
        int count;
        int []temps;
        int value;
        TempTracker()
        {
            mean=0.0;
            sum=0;
            count=0;
            min=Integer.MAX_VALUE;
            max=Integer.MIN_VALUE;
            count=0;
            mode=0;
            temps=new int[111];
            value=0;
        }

        // records a new temperature
        public void insert(int temperature) {
            count++;
            mode=0;
            value=0;
            sum+=temperature;
            if(temperature>max)
            {
                max=temperature;
            }
            if(temperature<min)
            {
                min=temperature;
            }
            temps[temperature]++;
            for(int i=0;i<111;i++)
            {
                if((temps[i])>mode)
                {
                    mode=temps[i];
                    value=i;
                }
            }
            mean=sum/count;
            
        }

        // returns the highest temp we've seen so far
        public int getMax() {
            
            return max;
        }

        // returns the lowest temp we've seen so far
        public int getMin() {
            return min;
        }

        // returns the mean of all temps we've seen so far
        public double getMean() {
            return (sum/count);
        }

        // return a mode of all temps we've seen so far
        public int getMode() {
            return value;
        }
    }

