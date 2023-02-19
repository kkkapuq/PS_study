package baekjun.src.baekjun.math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://st-lab.tistory.com/148 ����
//�ּڰ��� �Ƿ���, ���� ū���� ���־���ϴµ�,
//�׷��� ���ؼ�,
//����(-)�� �������� �и����ص�,
//�и��� ���ڿ����� ���� �����ش�.
//���� ������ ���� �������ش�.
public class Main1541 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sum = Integer.MAX_VALUE;
        String[] substraction = br.readLine().split("-");

        for(int i=0; i<substraction.length; i++){
            int temp = 0;

            //�������� ���� ��ū�� �������� �и��Ͽ� �ش� ��ū���� ���Ѵ�.
            String[] addition = substraction[i].split("\\+");

            //�������� ���� ��ū���� ��� ���Ѵ�.
            for(int j=0; j<addition.length; j++){
                temp += Integer.parseInt(addition[j]);
            }

            //ù��° ��ū�� ���, temp���� ù��° ���� ��.
            if(sum == Integer.MAX_VALUE){
                sum = temp;
            } else {
                sum -= temp;
            }
        }
        System.out.println(sum);

    }

}
