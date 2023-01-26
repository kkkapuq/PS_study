package baekjun.src.baekjun.greedy;

public class Pro01Test {
    public static void main(String[] args) {
        int[] food_times = {3,1,2};
        long k = 5;

        Pro01 p01 = new Pro01();

        int result = p01.solution(food_times, k);
        System.out.println(result);
    }
}
