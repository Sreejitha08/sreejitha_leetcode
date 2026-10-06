class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character>st=new Stack<>();
        for(Character c:s.toCharArray()){
            if (c=='(') st.push('(');
            else{
                if(!st.empty() && st.peek()=='(') st.pop();
                else st.push(c);
            }
        }
        return st.size();
    }
}