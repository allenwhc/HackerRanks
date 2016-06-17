#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <limits.h>
using namespace std;

void longestPalindromeSubsequence(string s, vector<vector<int>> &dp){
	if (s.empty()) return;
	int n = s.size();
	for (int i=0; i<n; i++) dp[i][i]=1;
	for (int k=2; k<=n; k++){
		for (int i=0; i<=n-k; i++){
			int j = i+k-1;
			if (s[i] == s[j] && k == 2) dp[i][j] = 2;
			else if(s[i] == s[j]) dp[i][j] = dp[i+1][j-1] + 2;
			else dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
		}
	}
}

int maxScore(string s){
	if (s.length() == 1) return 1;
	int score = 1;
	int n = s.length();
	vector<vector<int>> dp(n, vector<int>(n,0));
	longestPalindromeSubsequence(s, dp);
	for (int i=0; i<n-1; i++){
		score = max(score, dp[0][i] * dp[i+1][n-1]);
	}
	return score;
}

int main(int argc, char const *argv[])
{
	//string words = "jcaabdovmuiwsjkskeyifhfjxebwqbuqkndxmrxpqdbnpecgdh";
	//cout<<words.size()<<endl;
	string words = "qiquytyswjozmgagymqbbnehvrsqqxzowoftrnnmjylzfndofpzxlupoffndqspmfmbotnsosurfkneyrchzwewwxqpmgmsqsxsgukttjfvvssidjgftfwiqhgnvrvemiqyxnjjthgxrmqpvcksdugltoxrhjmnlvsohfyuvpymjthgscokxoxrzycqpcxubdzkexdaujrsxotbfmtoocvddpdinwczizylfvlacrvgrsaxthwvphaubhsipgeswoqxrkfpfzrmexxfxyzwzivnpolozeapcjuijczppntxuydrlbyrzgfrrdysticwrmlorcaipvtybnkmqoikkqowvcjrcqwksdxqfurfqormbyvisfatxlhlwxntgwijlcqxhtwagimarfdcbvknflzwtnnozdcacuavlitwvpwdgucjhhmpnguywwuzgswroedhszbvccobmzoagdjhyulnlgvdecfnysouzpjpllurswridjnedlmzzplkwxxrjfbzgwekovoigliysaddlqigexedurqemaeraeafcozbwhneamqruvqykpppdjsjfougwckobywuwhzevthyfxtwmbcjdimihjxurepnczsnpyfilpxeopkxhnqwphloxepjtbscnwyxlgsrbpyfsyimvhrvrwpimfiqobzepndzylobdrnewebrhfrmrqcmrsamdnhsofyfvmwtfboauewtgglkxzuyijmemedrjypeglbsblntbvtxzlqgunywhzxxovnuezobfhfsettqwtdrxxaxvhaegpaxmtjasewqufguwjzgbyvwcxnwbaukhrimqpuanohxtqrpywodyypcsjxovehqbshynyphtrkvwinedbewzjpswtmbhceuuqseqonzkabyzmkqkcavemcbaxxcngxczoaforkqiexjpqutqtnwklfvzcdakconvrwlppyytsjgetvsyfhbyvtjaimfssqbwehfoeiqxqsandkldrkswbsrwnqywolodrgvvztuswrgvqvhjvwhsuhkaffepckotoietaxawnjroyideawbkwsbhplnphtyzpcagqjkdybfczpkfvysjjqcwwfgnmeyytnvxezyyponnphdxkgcctbuzeicrogeafuyzapkbumhhvjwiebpcbuzuwylldsuaainshmkzopqhdxaxcxmuquevtweohsaqlewzuvrqkpwjwdunvucozrwilraijlqsixtkcqltermnkzvmqnijxnnisvstujlymplfsfbhjvhywjmrunvfxnkrgwzrgjzikegicqrbjdechjrwwmofmmggtlhkzmoqrzeuivtfxdavifnjkktqzdhtdayspebovzwanndvnqajupnsmvttbccgvgngavexdcnrlcttkayjewtmuonabaswstqxadebxlmyagphjzinyfivqdardsupejwsixsdtzbqcgwxyhwrgaogqjizivrrhsfwrjzcmbwdcnpjluqoahhwcvjpuduikmoqggeidyrrcjpfazpqqvwijbunfdlymlpkckvyljwwkxoynhausesnoofpcyisyqvdvisojmicrtelhkquhaiqcursjhtexvzlqosryrbjyrmnjdtliydjnsnotjsywjxiaqbtqkjrcmptkdihuxkwbsjpynfsaniqdokqsoqihrswcelodpzxldfxyldfncgrlqxotnrdgiitkadlzpemkxxljsbcwntjeyakgkcxdtdzmafvunjjevgvveeqgyglvwhutuepmeyflahcmuftemeuxnvlwzynvwooqlejwclxybanikftxuaaupbyhkjfjyenfsiazolcgvzfohbizlpyhxyfqneukoutigqkojxoxjpokhtqjjoobnxaozwcwlxbmuoieejndpkeobggoisywgkcsbqjouhcwziequwcgxdwplrqcrwvputitybrvreeuineqgcgiycoesivgpsiukcznxeoaiopgbuvyogxqcsgcuwcxatlmeibahjfpcesdlbuaofannqnljbdzfbgunqktgwvvmqdagaxwpahtzjfvkbrouztvwtsxwpmcthldwwvpatxszoxprdqffgfunlgucvhcmlrwhgzgyzzsnuohfvleatotetzqktyumugrwkxuclhxxglcxghbhyxkhzpeivdevjcedauhlpwsnggribvcohibzqxwnolmxqeseylwbfplkdyqdqhcagmfsfcsejeywocizxlnnnzofxcisxjymegmfmnyqcwujzkcqzabhggtomyowfycqqkfzfohwupqtgiuamanwexutsraipxvgwmawumjybtjyxuzaciuumoiltizrixcowdzdtbicptuxwbpuxxcnfviuznogbtmaruqjopkoikusfvwcxtvtpajkozwssvbozspkfmudysoqlsrnnuwyyznpmjiwuquvyxnqtnrkhpkynybaps";
	cout << maxScore(words) << endl;
	return 0;
}