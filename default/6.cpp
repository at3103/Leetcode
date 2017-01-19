
#include<iostream>
#include<stdlib>
#include<unordered_map>
#include<string>

class RandomizedSet {
public:
    int *data=NULL;
    std::unordered_map<std::string, int> index;
    int count;

    /** Initialize your data structure here. */
    RandomizedSet() {
        this->data = new int;
        //this->index["-1"] = 0;
        this->count=0;
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int value) {
        string val = std::to_string(value);
        if (!index[val])
        {   
            *(data+count) = value;
            index[val] = count+1;
            count++;
            return true;
        }
        else
            cout<<"error";
        return false;
        
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int value) {
        string val = std::to_string(value);
        string temp_val;
        int temp;
        if (!index[val])
            return false;
        else
        {
            std::swap(*(data+index[val]-1), *(data+count-1));
            temp = *(data+index[val]-1);
            temp_val  = std::to_string(temp);
            index[temp_val] = index[val];
            index[val] = 0;
            count--;
        }
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        
        if(count == 0)
            return -1;
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