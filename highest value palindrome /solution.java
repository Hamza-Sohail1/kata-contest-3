import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {
  
    public static String highestValuePalindrome(String s, int n, int k) {
    // Write your code here
        char[] c= s.toCharArray();
        
        //Try to make s a palindrome firtst
        for(int i=0; i<= n/2; i++)
        {
            int j= n-i-1;
            if(c[i] != c[j]){
                if(k<= 0)
                {
                    return "-1";
                }
                char max= c[i] > c[j] ? c[i] : c[j];
                c[i]= max;
                c[j]= max;
                k--;
            }
        }

        for(int i=0; k>0 && i<= n/2; i++)
        {                    System.out.println(k);

            int j= c.length-i-1;
            if( c[i]=='9' || c[j]=='9')
                continue;
            //If you changed a character to value !=9, undo, change it to 9, 
            //and change the corresponding character to 9 with one additional move  
            if(c[i] != s.charAt(i) || c[j]!= s.charAt(j) || i == j)
            {
                c[i]= '9';
                c[j]= '9';
                k--;
            }else{
                if(k>=2)
                {
                    c[i]='9';
                    c[j]= '9';
                    k-= 2;
                }
            }
            
        }
        return String.valueOf(c);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int k = Integer.parseInt(firstMultipleInput[1]);

        String s = bufferedReader.readLine();

        String result = Result.highestValuePalindrome(s, n, k);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
