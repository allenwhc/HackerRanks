#include <iostream>
#include <vector>
#include <numeric>
#include <string>
#include <fstream>
#include <istream>
using namespace std;

long long candy(vector<int> &ratings){
    if (ratings.empty()) return 0;
    int n = ratings.size();
    vector<int> candies(n, 1);
    for (int i=1; i<n; i++){
        if (ratings[i] > ratings[i-1]) 
            candies[i] = candies[i-1] + 1;
        else if (ratings[i] == ratings[i-1])
            candies[i] = 1;
    }

    for (int i=n-2; i>=0; i--){
        if (ratings[i] > ratings[i+1])
            candies[i] = max(candies[i], candies[i+1] + 1);
        else if (ratings[i] == ratings[i+1])
            candies[i] = max(candies[i], 1);
    }
    long long sum = 0;
    for (auto &c:candies) sum += c;
    return sum;
}

void match(int &a, int x, int &b, int y){
	
}

int main() {
    vector<int> ratings;
    string line;
    ifstream infile("/Users/haochenwang/Documents/Hackerranks/Algorithm/candies/data.txt");
    while (infile >> line){
    	ratings.push_back(stoi(line));
    }
    //for (auto &v: ratings) cout <<v <<endl;
    cout << candy(ratings) << endl;
    return 0;
}