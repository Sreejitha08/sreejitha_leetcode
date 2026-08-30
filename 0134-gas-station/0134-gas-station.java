class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalgas=0;
        int tank=0;
        int n=gas.length;
        int i;
        int start=0;
        for(i=0;i<n;i++){
            int diff=gas[i]-cost[i];
            totalgas+=diff;
            tank+=diff;
            if(tank<0){
                start=i+1;
                tank=0;
            }
        }
        if (totalgas>=0) return start;
        return -1;
    }
}