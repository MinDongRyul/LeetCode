class Solution {
public:
    string multiply(string num1, string num2) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int m = num1.length();
        int n = num2.length();
        if(m==0||n==0){
            return "";
        }
        string result(m+n,'0');
        int carry = 0;
        int curr = 0;
        int k = 0;
        for(int j=n-1;j>=0;j--){
            k = m+j;
            for(int i=m-1;i>=0;i--){
                curr = static_cast<int>(num1[i]-'0')*static_cast<int>(num2[j]-'0')+carry+static_cast<int>(result[k]-'0');
                result[k] = static_cast<char>(curr%10)+'0';
                carry = curr/10;
                k--;
            }
            if(carry!=0){
                result[k] = static_cast<char>(carry)+'0';
                carry = 0;
            }
        }
        
        for(int i=0;i<m+n;i++){
            if(result[i] !='0'){
                return result.substr(i,m+n-i);
            }
        }
        return "0";
    }
};