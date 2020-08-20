class LRUCache {
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
       if (values.find(key) == values.end()) {
           return -1;
       }
        
       order_used.erase(positions[key]);
       order_used.push_back(key);
       positions[key] = --(order_used.end());
        
       return values[key]; 
    }
    
    void put(int key, int value) {
        if (values.find(key) != values.end()) {
            order_used.erase(positions[key]);
            values[key] = value;
            positions.erase(key);
        }
        else {
            values.insert({key, value});
        }
        
        order_used.push_back(key);
        positions.insert({key, --(order_used.end())});
        
        if (order_used.size() > capacity) {
            int key = *order_used.begin();
            order_used.erase(order_used.begin());
            positions.erase(key);
            values.erase(key);
        } 
    }
private:
    int capacity;
    list<int> order_used;
    
    unordered_map<int, list<int>::iterator> positions;
    unordered_map<int, int> values;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
