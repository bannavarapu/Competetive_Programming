import java.util.*;

public class Problem1{
	
	 public static void main(String[] args) {

	 	Scanner sc = new Scanner(System.in);

	 	while(sc.hasNext()){
	 	String s1 = sc.nextLine();
	 	String s2 = sc.nextLine();
	 	s1=s1.toLowerCase();
	 	s2=s2.toLowerCase();

	 	char []c1 = s1.toCharArray();
	 	char []c2 = s2.toCharArray();

	 	// Arrays.sort(c1);
	 	// Arrays.sort(c2);

	 	int c = 0;
	 	for(int i=0;i<c1.length;i++){
	 		if(c1[i]!=' ')
	 		c=c^c1[i];
	 	}
	 	for(int i=0;i<c2.length;i++){
	 		if(c2[i]!=' ')
	 		c=c^c2[i];
	 	}
	 	if(c==0)
	 		System.out.println("True");
	 	else
	 		System.out.println("False");

	 	}
	
		
	}
}