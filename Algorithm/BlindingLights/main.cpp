#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <limits.h>
using namespace std;

vector<vector<long>> shortestDistance(vector<vector<long>> &graph){
	vector<vector<long>> distance(graph);
	int n = graph.size();
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			for(int k = 0; k < n; k++){
				distance[j][k] = min(distance[j][i] + distance[i][k], distance[j][k]);
			}
		}
	}
	return distance;
}

int main(int argc, char* argv[]){
	int n = 4, m = 5;
	vector<vector<long>> graph = {{0, 5, INT_MAX, 24}, {INT_MAX, 0, INT_MAX, 6}, {INT_MAX, 7, 0, 4}, {INT_MAX, INT_MAX, INT_MAX, 0}};
	vector<vector<long>> distance = shortestDistance(graph);
	for (auto &vv: distance){
		for(auto &v:vv)
			cout << v << " ";
		cout << endl;
	}
	int q = 3;
	vector<vector<int>> query = {{0,1},{2,0},{0,3}};

	for (int i=0; i<query.size(); i++)
		cout << distance[query[i][0]][query[i][1]] << endl;
	return 0;
}