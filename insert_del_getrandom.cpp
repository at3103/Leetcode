
#include<iostream>
#include<stdlib>
#include<unordered_map>

class RandomizedSet {
public:
    int *data=NULL;
    std::unordered_map<int, int> index;
    int count;
    /** Initialize your data structure here. */
    RandomizedSet() {
        this->data = new int[10000];
        this->index[-1] = 0;
        this->count=0;
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
            bool flag = false;
            if (!index[val])
            {
                *(data+count) = val;
                index[val] = count+1;
                count++;
                flag = true;
            }
            return flag;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (!index[val])
            return false;
        else
        {
            std::swap(*(data+index[val]-1), *(data+count-1));
            index[*(data+index[val]-1)] = index[val];
            index[val] = 0;
            count--;
        }
        return true;
        
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int n;
        n = count == 1 ? count : count - 1;
        int ind = rand()%(count);
        return *(data +ind);
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */