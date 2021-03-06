package main

import (
	"math/rand"
	"time"
)

/*
	questions to ask:
	- each item means each the items inserted or the key inserted? allow duplicate?

	1st approach: hashtable

	Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		O(n)
	Space							O(n) the unique keys
	1336 ms, faster than 6.52%
*/

type RandomizedSet struct {
	HashTable map[int]bool
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{make(map[int]bool)}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
	if _, x := this.HashTable[val]; x {
		return false
	}
	this.HashTable[val] = true
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	if _, x := this.HashTable[val]; x {
		delete(this.HashTable, val)
		return true
	}
	return false
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	rand.Seed(time.Now().UTC().UnixNano())
	n := len(this.HashTable)
	targetIdx := rand.Intn(n)
	keys := []int{}
	for k, _ := range this.HashTable {
		keys = append(keys, k)
	}
	key := keys[targetIdx]
	return key
}

/*
	learned from others
	2nd approach: hashtable + array
	- save value: index in hashtable
	- when delete, swap the target item and the last item in the array, and remove the last item
	- see ./idea_add.png and ./idea_remove.png

	Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		O(1)
	Space							O(n) the unique keys
	32 ms, faster than 100.00%
*/

type RandomizedSet1 struct {
	HashTable map[int]int
	Arr       []int
}

/** Initialize your data structure here. */
func Constructor1() RandomizedSet1 {
	return RandomizedSet1{make(map[int]int), []int{}}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet1) Insert(val int) bool {
	if _, x := this.HashTable[val]; x {
		return false
	}
	this.HashTable[val] = len(this.Arr)
	this.Arr = append(this.Arr, val)
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet1) Remove(val int) bool {
	if _, x := this.HashTable[val]; x {
		// find the target index of the val from the hashtable
		targetIdx := this.HashTable[val]
		// assign the last item to the target index
		this.HashTable[this.Arr[len(this.Arr)-1]] = targetIdx
		// swap the target item and the last item
		this.Arr[targetIdx], this.Arr[len(this.Arr)-1] = this.Arr[len(this.Arr)-1], this.Arr[targetIdx]
		// remove the last item
		this.Arr = this.Arr[:len(this.Arr)-1]
		// delete the key from hashtable
		delete(this.HashTable, val)
		return true
	}
	return false
}

/** Get a random element from the set. */
func (this *RandomizedSet1) GetRandom() int {
	r := rand.Intn(len(this.Arr))
	return this.Arr[r]
}

func main() {
	c := Constructor1()
	c.Insert(1)
	c.Insert(2)
	c.Insert(3)
	c.Remove(1)
	c.Remove(2)
	c.Remove(3)
}
