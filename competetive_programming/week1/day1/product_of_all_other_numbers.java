public class Solution {

    public static int[] getProductsOfAllIntsExceptAtIndex(int[] intArray) {

        // make an array of the products
        int l=intArray.length;
        if(l==1)
        {
            return null;
        }
        int [] left= new int[l];
        int [] right= new int[l];
        int [] result= new int[l];
        left[0]=1;
        right[l-1]=1;
        for(int i=1;i<l;i++)
        {
          result[i]=left[i-1]*intArray[i-1];  
        }
        for(int j=l-2;j>=0;j--)
        {
            result[j]=right[l+1]*intArray[l+1];
        }
        for(int i=0;i<l;i++)
        {
            result[i]=left[i]*right[i];
        }

        return result;
    }

