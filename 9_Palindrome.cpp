class Solution {
public:
    bool isPalindrome(int x) {

        int flag = 1,l=1;
        
        if(x<0)
            return false;

        while(1)
        {
            if(!(x/int(pow(10,l))))
                break;
            l++;
        }
        for (int i=1,j=l-1; x>0; i++,j-=2)
        {
            if(x%10!=(x/int(pow(10,j))))
            {
                flag=0;
                break;
            }
            x/=10;
            if(x)
                x%=(int)pow(10,j-2);
        }
        
        return bool(flag);
        
    }
};