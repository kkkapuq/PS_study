package baekjun.DFSBFS;

import java.io.*;
import java.util.*;

public class Main266702 {
	
	static int n, cnt, h;
	static ArrayList<Integer> home = new ArrayList<Integer>();
	static int[][] map;
	static boolean[][] visited;
	static int[][] dir = {{-1,0},{1,0},{0,-1},{0,1}};
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new int[n][n];
		visited = new boolean[n][n];
		for(int i=0; i<n; i++) {
			String st = br.readLine();
			for(int j=0; j<st.length(); j++) {
				map[i][j] = st.charAt(j) - '0';
			}
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(!visited[i][j] && map[i][j] == 1) {
					dfs(i,j);
					cnt += 1;
					home.add(h);
					h = 0;
				}
			}
		}
		
		Collections.sort(home);
		sb.append(cnt).append('\n');
		for(int i=0; i<home.size(); i++) {
			sb.append(home.get(i)).append('\n');
		}
		System.out.println(sb);
		
		
	}
	
	static void dfs(int x, int y) {
		visited[x][y] = true;
		h += 1;
		
		for(int i=0; i<4; i++) {
			int nx = x + dir[i][0];
			int ny = y + dir[i][1];
			
			if(nx < 0 || ny < 0 || nx >= n || ny >= n) {
				continue;
			}
			
			if(!visited[nx][ny] && map[nx][ny] == 1) {
				dfs(nx, ny);
			}
		}
	}

}
