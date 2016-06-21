#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <limits.h>
#include <algorithm>
using namespace std;

vector<pair<int,int>> findMinDiff(vector<int> &arr){
    if(arr.size()<2) return {};
    vector<pair<int,int>> res;
    int min_diff = INT_MAX;
    for(int i=1; i<arr.size(); i++){
        int diff = arr[i] - arr[i-1];
        if (diff>min_diff) continue;
        else if(diff == min_diff) res.push_back(make_pair(arr[i-1], arr[i]));
        else{
            min_diff = diff;
            res.clear();
            res.push_back(make_pair(arr[i-1],arr[i]));
        }
    }
    return res;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n; 
    cin >> n;
    vector<int> arr;
    for (int i=0; i<n; i++){
        int x;
        cin >> x;
        arr.push_back(x);
    }
    sort(arr.begin(), arr.end());
    vector<pair<int,int>> res = findMinDiff(arr);
    for(auto &v: res)
        cout << v.first << " " << v.second << " ";
    return 0;
}