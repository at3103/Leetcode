
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector <int> maxel;
        int temp;
        if (nums.size() == 0)
            return nums;
        if (k == 1)
            return nums;
        temp = (*std::max_element(nums.begin(),nums.begin()+k));
        maxel.push_back(temp);
        for (int i=1;i<nums.size()-k+1;i++)
        {
            if (nums[i+k-1] >= temp)
            {
                temp = nums[i+k-1];
                maxel.push_back(temp);
                continue;
            }
            else if (nums[i-1] != temp)
            {
                maxel.push_back(temp);
                continue;
            }

            temp = (*std::max_element(nums.begin()+i,nums.begin()+i+k));   
            maxel.push_back(temp);
        }
     
        return maxel;   
    }
};