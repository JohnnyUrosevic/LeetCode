class RandomizedCollection {
        
private:
    vector<int*> vals;
    //maps val to index of counts
    unordered_map<int, vector<int>> collection;

public:
    /** Initialize your data structure here. */
    RandomizedCollection() {}
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        auto it = collection.find(val);
        bool newElement = it == collection.end() || it->second.empty();
        
        collection[val].push_back(vals.size());
        vals.push_back(new int(val));
        
        return newElement;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        auto it = collection.find(val);
        
        if (it == collection.end() || it->second.empty()) {
            return false;
        }
        delete vals[it->second[it->second.size() - 1]];
        vals[it->second[it->second.size() - 1]] = nullptr;
        it->second.erase(it->second.end() - 1);
        return true;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        int* val;
        
        do {
            val = vals[rand() % vals.size()];
        } while(val == nullptr);
        
        return *val;
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
