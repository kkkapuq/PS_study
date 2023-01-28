package Programmers;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Solution42891 {
	
	class Food {
		int time,idx;
		
		Food(int t, int i){
			time = t;
			idx = i;
		}
	}
	
	Comparator<Food> time = new Comparator<Food>() {
		public int compare(Food a, Food b) {
			return a.time - b.time;
		}
	};
	
	Comparator<Food> idx = new Comparator<Food>() {
		public int compare(Food a, Food b) {
			return a.idx - b.idx;
		}
	};

	public int solution(int[] food_times, long k) {
		
		List<Food> foods = new ArrayList<Food>();
		for(int i=0; i<food_times.length; i++) {
			foods.add(new Food(food_times[i], i+1));
		}
		
		foods.sort(time);
		
		int n = food_times.length;
		long prevtime = 0;
		
		for(int i=0; i<food_times.length; i++) {
			long diff = foods.get(i).time - prevtime;
			
			if(diff != 0) {
				long spend = diff * n;
				if(k >= spend) {
					k -= diff * n;
					prevtime = foods.get(i).time;
				} else {
					foods.subList(i, food_times.length).sort(idx);
					k %= n;
					return foods.get(i + (int)k).idx;
				}
			}
			n--;
		}
        
        return -1;
    }

}
