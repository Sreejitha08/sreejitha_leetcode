/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        ArrayList<Integer> a=new ArrayList<>();
        ListNode temp=head;
        while(temp!=null){
            a.add(temp.val);
            temp=temp.next;
        }
        ArrayList<Integer> res=new ArrayList<>();
        int i;
        for(i=1;i<a.size()-1;i++){
            if((a.get(i)>a.get(i-1) && a.get(i)>a.get(i+1)) || (a.get(i)<a.get(i-1) && a.get(i)<a.get(i+1))){
                res.add(i);
            }
        }
        int mini=Integer.MAX_VALUE;
        int []result=new int[2];
        result[0]=-1;
        result[1]=-1;
        if (res.size()<2){
            return result;
        }
        result[1]=res.get(res.size()-1)-res.get(0);
        for(i=0;i<res.size()-1;i++){
            mini=Math.min(mini,res.get(i+1)-res.get(i));
        }
        result[0]=mini;
        return result;
    }
}