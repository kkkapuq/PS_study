package baekjun.src.baekjun.greedy;

public class Pro01 {
    public int solution(int[] food_times, long k) {

        long time = 0; int i = 0, len = food_times.length - 1, cnt = 0;
        while(true){
            if(i == len + 1){
                i = 0;
            }


            if(k == time){
                break;
            }

            if(food_times[i] != 0){
                food_times[i]--;
                time += 1;
            } else {
                cnt += 1;
            }
            i++;
        }

        if(cnt == food_times.length){
            return -1;
        } else {
            return i;
        }
    }
}
