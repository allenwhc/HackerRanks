#include <iostream>
#include <fstream>
#include <numeric>
#include <vector>
using namespace std;

void dfs(vector<vector<int>> &adj, vector<int> &value, int u, int p, int &min_diff, int total){
    for(auto &v:adj[u]){
        if(v != p){
            dfs(adj, value, v, u, min_diff, total);
            value[u] += value[v];
        }
    }
    if(u != 0)
        min_diff = min(min_diff, abs(total - 2*value[u]));
}

int getMinCut(int n, vector<int> &value, vector<pair<int, int>> &edges){
    vector<vector<int>> adj(n);
    for(auto &e: edges){
        adj[e.first].push_back(e.second);
        adj[e.second].push_back(e.first);
    }
    int result = INT_MAX;
    dfs(adj, value, 0, 0, result, accumulate(value.begin(), value.end(), 0));
    return result;
}

int main(int argc, char *argv[]){
	ifstream infile("/Users/haochenwang/Documents/Hackerranks/Algorithm/CutTree/data.txt");
	int a, b;
	string line;
	vector<string> data;
	while (infile >> line){
		data.push_back(line);
	}
	int n = stoi(data[0]);
	vector<int> weight;
	vector<pair<int, int>> edges;
	for(int i=1; i<n+1; i++) weight.push_back(stoi(data[i]));
	for(int i=n+1; i<data.size(); i+=2) edges.push_back(make_pair((stoi(data[i])-1), (stoi(data[i+1]) - 1)));
	// for(vector<pair<int,int>>::iterator it=edges.begin(); it!=edges.end(); it++)
 //        cout<<it->first<<","<<it->second<<endl;
	cout<<getMinCut(n, weight, edges)<<endl;
	return 0;
}
