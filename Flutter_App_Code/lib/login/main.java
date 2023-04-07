import java.util.*;
import java.math.*;

public class main{
  
  final static Scanner scan = new Scanner(System.in);
  
  public static void main(String[] ars){
    
    int a,b,y,z;
    
    a = scan.nextInt();
    b = scan.nextInt();
    y = scan.nextInt();
	  z = scan.nextInt();
    
    a =   (int) (a*Math.pow(10,b));
    y =  (int) (y*Math.pow(10,z));

    if(a<y){
      a=y;
    }

    System.out.print(a);
  }
}