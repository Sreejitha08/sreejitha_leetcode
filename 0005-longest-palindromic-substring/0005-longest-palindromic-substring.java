class Solution {
    public String longestPalindrome(String s) {
        int i;
        int start=0;
        int c=0;
        int maxi=0;
        String res="";
        int n=s.length();
        for(i=0;i<n;i++){
            int l=i,r=i;
            while(l>=0 && r<n && s.charAt(l)==s.charAt(r)){
                l--;
                r++;
            }
            if ((r-l+1)>maxi){
                maxi=r-l+1;
                start=l;
                res=s.substring(l+1,r);
            }
            l=i;r=i+1;
            while(l>=0 && r<n && s.charAt(l)==s.charAt(r)){
                l--;
                r++;
            }
            if ((r-l+1)>maxi){
                maxi=r-l+1;
                start=l;
                res=s.substring(l+1,r);
            }
        }
        return res;
    }
}