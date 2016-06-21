#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

int countPairs(vector<int> &nums){
	if(nums.size()<2) return 0;
	unordered_map<int,int> mp;
	for(auto &x:nums) mp[x]++;
	int count=0;
	for(auto it=mp.begin(); it!=mp.end(); it++){
		if(it->second>1) count += (it->second)*(it->second-1);
	}
	return count;
}

int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
	vector<int> nums = {671,949,460,546,634,679,496,533,825,173};
	
	return 0;
}
