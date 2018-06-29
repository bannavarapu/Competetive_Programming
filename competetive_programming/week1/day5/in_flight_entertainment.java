public static boolean canTwoMoviesFillFlight(int[] movieLengths, int flightLength) {

        // determine if two movies add up to the flight length
        HashMap<Integer,Integer>hm= new HashMap<>();
        int count=0;
        for(int i=0;i<movieLengths.length;i++)
        {
            if(hm.containsKey(movieLengths[i]))
            {
                int x= hm.get(movieLengths[i]);
                x=x+1;
                hm.put(movieLengths[i],x);
            }
            else
            {
                hm.put(movieLengths[i],1);
            }
        }
        for(int i: movieLengths)
        {
         try
         {
            int x=(hm.get(flightLength-i));
            if((flightLength-i)==i)
            {
                if(x>1)
                {
                	count++;
                }
            }
            else
            {
            	count++;
            }
         }
         catch(Exception e)
         {
//             System.out.println(e.getMessage());
         }
        }
        if(count>0)
        return true;
        else
        return false;
    }
