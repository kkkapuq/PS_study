package baekjun.BackTrack;

import java.io.*;
import java.util.*;

//1. 치킨집들의 위치를 chicken배열에 담아준다.
//2. 집들의 위치를 houses배열에 담아준다.
//3. chicken_visited를 이용하여 이 배열의 idx를 활용해 치킨집을 뽑았는지 뽑지 않았는지를 표현한다.

public class Main15686 {
	
	static int n,m,min = Integer.MAX_VALUE;
	static StringTokenizer st;
	static int[][] graph;
	static ArrayList<Node> chicken = new ArrayList<Node>();
	static ArrayList<Node> houses = new ArrayList<Node>();
	static boolean[] chicken_visited; //뽑은 치킨집 체크
	
	static class Node{
		int x,y;
		
		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		graph = new int[n+1][n+1];
		for(int i=1; i<=n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=1; j<=n; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if(graph[i][j] == 1) {
					houses.add(new Node(i,j));
				} else if(graph[i][j] == 2) {
					chicken.add(new Node(i,j));
				}
			}
		}
		
		chicken_visited = new boolean[chicken.size()];
		backtrack(0,0);
		System.out.println(min);
	}
	
	static void backtrack(int count, int idx) {
		//치킨 거리의 최솟값을 구한다.
		if(count == m) {
			int total = 0;
			for(int i=0; i<houses.size(); i++) {
				int distance = Integer.MAX_VALUE;
				for(int j=0; j<chicken.size(); j++) {
					if(chicken_visited[j]) {
						int dist = Math.abs(houses.get(i).x - chicken.get(j).x) + Math.abs(houses.get(i).y - chicken.get(j).y);
						distance = Math.min(distance,dist);
					}
				}
				total += distance;
			}
			min = Math.min(total, min);
			return;
			
		}
		
		
		for(int i=idx; i<chicken.size(); i++) {
			if(!chicken_visited[i]) {
				chicken_visited[i] = true;
				backtrack(count + 1, i + 1);
				chicken_visited[i] = false;
			}
		}
	}

}
