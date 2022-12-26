"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


LRU cache:
最近最少使用缓存。
维基百科：https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU

在capacity满后，有新数据加入时使用次数最低且最先被加入的一个会被删除。

我的思路是：
1. 给每一个数据带权重。
1.1  capacity 未满时：
1.1.1 若是不重复的数据则直接添加，{key: {value, weight}}
1.1.2 若已重复则更新权重。

2. 根据权重在满数据时删除。
2.1 数据已满之后：
2.1.1 若是已重复的则更新权重。
2.1.2 若是未重复的则删除权重最低的一个，并将新数据添加 {key: {value, weight}}。

权重问题：
每次有更新，新增，权重就会增加1，无上限。

---
第一版实现，并通过测试：
https://leetcode.com/problems/lru-cache/description/

效率还可以。beat 25% 左右。


"""

c.. LRUCache o..

    ___ __init__  capacity
        """
        :type capacity: int
        """
        self.lru_cache _ # dict
        self.lru_cache_number _ # dict
        self.current_cache_number = 0
        self.capacity = capacity

    ___ get  key
        """
        :type key: int
        :rtype: int
        """
        r_ self._get(key)
        
    ___ _get  key
        # if inexistent then return -1
        # or add weight and return value
        value = self.lru_cache.get(key)
        __ n.. value:
            r_ -1
        ____
            self._add_exist_key_weight(key)
            r_ value.get('value')
            
    ___ _add_exist_key_weight  key
        # remove raw weight and add new weight
        data = self.lru_cache.get(key)
        raw_weight = data.get('weight')
        data['weight'] = self.current_cache_number
        
        self.lru_cache_number.pop(raw_weight)
        self.lru_cache_number[self.current_cache_number] = key
        self.current_cache_number += 1
        
    ___ put  key, value
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        # check capacity
        # True will run clear
        # Then put data.
        is_reached_capacity = self.check_cache_capacity()
        __ n.. is_reached_capacity:
            __ self.lru_cache.get(key
                self._replace(key, value)
            ____
                self._put(key, value)
        ____
            __ self.lru_cache.get(key
                self._replace(key, value)
            ____
                self._put_and_remove(key, value)
            
    ___ _put  key, value
        """
            {
                key: {'value': value, 
                      'weight': self.current_cache_number}
            }
            {
                weight: key
            }
        """
        self.lru_cache[key] = {'value': value, 'weight': self.current_cache_number}
        self.lru_cache_number[self.current_cache_number] = key

        self.current_cache_number += 1

    ___ _put_and_remove  key, value
        # remove the least key and put the new key.
        
        min_weight = m.. self.lru_cache_number)


        self.lru_cache.pop(self.lru_cache_number[min_weight])
        self.lru_cache_number.pop(min_weight)
        self._put(key, value)
  
    ___ _replace  key, value
        """
            replace the existed key to new value and weight.
        """
        
        raw_data = self.lru_cache.get(key)
        raw_weight = raw_data.get('weight')
        
        raw_data['value'] = value
        raw_data['weight'] = self.current_cache_number
        
        self.lru_cache_number.pop(raw_weight)
        self.lru_cache_number[self.current_cache_number] = key
        self.current_cache_number += 1
    
    ___ check_cache_capacity(self
        """
            True is reached capacity.
            False is not.
        """
        __ l..(self.lru_cache) __ self.capacity:
            r_ True
        
        r_ F..
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)