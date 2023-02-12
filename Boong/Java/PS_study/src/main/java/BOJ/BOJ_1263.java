import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

import static java.lang.Math.min;

public class BOJ_1263 {
    public static void main(String[] args) throws IOException {

        /**
         * 1. t = 걸리는 시간, s = 끝내야 하는 시간
         * 2. 마찬가지로 끝내야 하는 시간을 오름차순으로 정렬 후,
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        // 2차원 배열로 i번째 인덱스에 t와 s를 집어넣어준다.
        int[][] workList = new int[n][2];

        for (int i = 0; i < n; i++) {
            String[] temp = br.readLine().split(" ");
            workList[i][0] = Integer.parseInt(temp[0]);
            workList[i][1] = Integer.parseInt(temp[1]);
        }

        // s 기준으로 오름차순 정렬
        Arrays.sort(workList, (a1, a2) -> {
            if (a1[0] == a2[2]) {
                return Integer.compare(a1[1], a2[1]);
            } else {
                return Integer.compare(a1[0], a2[0]);
            }
        });

        int startTime = 0;

        //
        for (int i = 0; i < workList.length; i++) {
            int curTime = workList[i][0];
            for (int j = 0; j < i; j++) {
                curTime += workList[j][0];
            }
            if (workList[i][1] < curTime) {
                System.out.println(-1);
                break;
            } else {
                startTime = min(startTime, workList[i][1] - curTime);
            }
        }
        bw.write(startTime);

        bw.flush();
        bw.close();
    }

}
