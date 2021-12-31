// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int N, int K){
        if(N >= K) return 1;
        int sumN = N*(N+1)/2;
        if(sumN < K){
            return -1;
        }else if(sumN == K){
            return N;
        }else{
            int water = N;
            int maxCapacity = K;
            Set<Integer> usedGlasses = new HashSet<>();
            while(maxCapacity > 0){
                int toFill = Math.min(water, maxCapacity);
                for (int i = toFill; i > 0; i--) {
                    if(!usedGlasses.contains(i)){
                        usedGlasses.add(i);
                        maxCapacity -= i;
                        break;
                    }
                }
            }
            return usedGlasses.size();
        }
    }
}
