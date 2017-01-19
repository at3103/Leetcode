#include<iostream>
#include<stdlib>
#include<unordered_map>

struct values{
  int val[25];
  int count;
};

class RandomizedCollection {
public:
    /** Initialize your data structure here. */
    int *data=NULL;
    std::unordered_map<int, struct values> index;
    int count;
    RandomizedCollection() {
        this->data = new int[10000];
        struct values v;
        v.count = 0;
        v.val[count]=0;
        this->index[-1] = v;
        this->count=0;
        
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        bool flag = false;
        if (!index[val].count)
            flag = true;
            
        *(data+count) = val;
        index[val].val[count] = count+1;
        index[val].count++;
        count++;

        return flag;
        
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        if (!index[val].count)
            return false;
        else
        {
            std::swap(*(data+index[val].val[count-1]-1), *(data+count-1));
            index[*(data+index[val].val[count-1]-1)] = index[val].val[count-1];
            index[val] = 0;
            count--;
        }
        return true;   
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        int n;
        n = count == 1 ? count : count - 1;
        int ind = rand()%(count);
        return *(data +ind);
        
    }
};



/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */