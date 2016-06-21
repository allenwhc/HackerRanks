#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    vector<int> arr;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        arr.push_back(x);
    }
    vector<int> anomaly;
    for(int i=1; i<arr.size(); i++){
        if(arr[i]<arr[i-1]){
            if(anomaly.size()<2 || i-anomaly.back()-1 == 1) 
                anomaly.push_back(i-1);
            else{
                cout <<"no"<< endl;
                return 0;
            }
        }   
    }
    if(anomaly.empty()) {
        cout << "yes" << endl;
        return 0;
    }
    int sz = anomaly.size(), l = anomaly[0], r = anomaly.back()+1;
 //   string res = "";
    if((!l || arr[r]>=arr[l-1]) && (r==n-1 || arr[l]<=arr[r+1])){
        cout << "yes" << endl;
        if(sz>2) cout << "reverse ";
        else cout << "swap ";
        cout << l+1 <<" " << r+1 << endl;
    }else{
        cout << "no" << endl;
    }
    return 0;
}