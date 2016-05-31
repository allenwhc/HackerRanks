#include <vector>
#include <math.h>
using namespace std;

bool isSquare(int n){
	long root= (long) sqrt(n);
	return n==root*root;
}

vector<int> getCollections(int n){
	vector<int> res;
	int count=0;
	long a,b,c,d,e,f;
	for (int i=4; count<n; i++){
		a=i*i;
		for (int j=3; j<i && count<n; j++){
			c=j*j; 
			f=a-c;
			if (f<=0 || !isSquare(f)) continue;
			long k=(j % 2)==1?1:2
			for (k; k<j; k+=2){
				d=k*k;
				e=a-d;
				b=c-e;
				if (b<=0 || !isSquare(b) || e<=0 || !isSquare(e)) continue;
				long x=(d+c)/2;
				long y=(e+f)/2;
				long z=(c-d)/2;
				result.push_back({x,y,z});
				count++;
				break;
			}
		}
	}
}

int main(int argc, char *argv[]){
	int n=1;
	vector<int> result=getCollections(n);
	for (auto &v:result)
	{
		for (vector<int>::iterator it=v.begin(); it!=v.end(); it++)
			cout<<*it<<" ";
	}
}
