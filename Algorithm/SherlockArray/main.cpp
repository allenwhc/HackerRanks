#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;

string divide(vector<int> &nums, int sum){
    if(nums.size()==1) return "YES";
    int left_sum=0, right_sum=sum;
    for(int i=1; i<nums.size(); i++){
        left_sum += nums[i-1];
        right_sum -= nums[i];
        if(left_sum == right_sum) return "YES";
    }
    return "NO";
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    cin >> T;
    while (T--){
        int n;
        cin >> n;
        vector<int> nums;
        int sum = 0;
        for(int i=0; i<n; i++){
            int x;cin>>x;nums.push_back(x);
            sum+=x;
        }
        cout << divide(nums, sum-nums[0]) << endl;
    }
    return 0;
}
