package boj7569;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int n, m, h;
    static int dx[] = { 1, -1, 0, 0, 0, 0 };
    static int dy[] = { 0, 0, 1, -1, 0, 0 };
    static int dz[] = { 0, 0, 0, 0, 1, -1 };

    static int tomato[][][];
    static int dist[][][];
    static Queue<Location> q = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        tomato = new int[n][m][h];
        dist = new int[n][m][h];
        initArr(dist, -1);

        for (int k = 0; k < h; k++) {
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < m; j++) {
                    tomato[i][j][k] = Integer.parseInt(st.nextToken());
                    if (tomato[i][j][k] == 1) {
                        q.add(new Location(i ,j , k));
                        dist[i][j][k] = 0;
                    }
                }
            }
        }

        while(!q.isEmpty()) {
            Location cur = q.poll();

            for (int i = 0; i < 6; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                int nz = cur.z + dz[i];

                if (isRange(nx, ny, nz) && tomato[nx][ny][nz] == 0 && dist[nx][ny][nz] == -1) {
                    tomato[nx][ny][nz] = 1;
                    dist[nx][ny][nz] = dist[cur.x][cur.y][cur.z] + 1;
                    q.add(new Location(nx, ny, nz));
                }
            }
        }


        if (!checkTomato()) {
            System.out.println(-1);
            return;
        }

        System.out.println(getMax());

    }

    static boolean checkTomato() {
        for (int k = 0; k < h; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (tomato[i][j][k] == 0) return false;
                }
            }
        }
        return true;
    }

    static int getMax() {
        int max = 0;
        for (int k = 0; k < h; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (dist[i][j][k] > max) max = dist[i][j][k];
                }
            }
        }
        return max;
    }

    static boolean isRange(int x, int y, int z) {
        return x >= 0 && y >= 0 && z >= 0 && x < n && y < m && z < h;
    }

    static void initArr(int arr[][][], int val) {
        for (int k = 0; k < h; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    arr[i][j][k] = val;
                }
            }
        }
    }

    static class Location {
        int x, y, z;

        public Location(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }
}
