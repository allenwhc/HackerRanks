#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;

int maxPeople(vector<vector<int>> &buildings, int n, int h, int d){
	vector<vector<int>> ppl(n, vector<int>(h+1, 0));
	
	//Calculate distribution of ppl trapped in building
	//ppl[i][j] -> # of ppl trapped on jth floor in ith building
	for (int i=0; i<n; i++){
		for(int j=0; j<buildings[i].size(); j++)
			ppl[i][buildings[i][j]]++;
	}
	vector<vector<int>> f(ppl);
	vector<int> ppl_by_floor(h+1, 0);	// ppl_by_floor store the maximum people on each floor among different buildings
	for (int i=0; i<n; i++) ppl_by_floor[h] = max(ppl_by_floor[h], f[i][h]);	//First, count max ppl on top floor

	for (int j = h - 1; j >= 0; j--){
		for(int i = 0; i < n; i++){
			int tmp = 0;
			if (j + d <= h) tmp = max(tmp, ppl_by_floor[j + d]);
			tmp = max(tmp, f[i][j + 1]);
			f[i][j] = tmp + ppl[i][j];
			ppl_by_floor[j] = max(ppl_by_floor[j], f[i][j]);
		}
	}
	int res = 0;
	for (int i = 0; i < n; i++) res = max(res, f[i][0]);
	return res;
}

int main(int argc, char const *argv[])
{
	int n = 4, h = 15, d = 2;
	vector<vector<int>> buildings = {{1,1,1,4,10},{9,5,7,7,3,9,8,8},{9,5,6,4,3},{}};
	cout << maxPeople(buildings, n, h, d) << endl;
	return 0;
}