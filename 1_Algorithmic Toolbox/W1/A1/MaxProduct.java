import java.util.*;
import java.io.*;
import java.util.Scanner;

public class MaxProduct{

    static long MAX(long[] numbers){
        int n = numbers.length;
        int maxindex1 = -1;
        for (int i = 0; i < n; i++){
        if(maxindex1 == -1 || numbers[i] > numbers[maxindex1])
        maxindex1 = i;
    }

    int maxindex2 = -1;
    for (int i = 0; i < n; i++){
        if(i == maxindex1)
        continue;

        if(maxindex2 == -1 || numbers[i] > numbers[maxindex2])
        maxindex2 = i;
    }
    return (( long) numbers[maxindex1] * numbers[maxindex2]);



    }


public static void main(String[] args)
{
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    long[] numbers = new long[n];
    for (int i = 0; i < n; i++){
        numbers[i] = input.nextLong();
    }

    System.out.println(MAX(numbers));

    
}
}