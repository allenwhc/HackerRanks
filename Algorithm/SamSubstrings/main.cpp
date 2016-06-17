#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

long long sumOfSubstring(string x){
	int mod = pow(10,9) + 7;
	int n = x.length();
	long long result = 0;
	long long base = 1;
	for (int i = n-1; i>=0; i--){
		result = (result + (x[i] - '0')*base*(i+1)) % mod;
		base = (base*10+1) % mod;
	}
	return result;
}

int main(int argc, char* argv[]){
	string x = "123";
	cout << "sum of substring is: " << sumOfSubstring(x) << endl;
}