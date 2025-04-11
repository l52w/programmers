#include <string>
#include <vector>
#include <numeric>
using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    int numer , denom;
    int gcd_num;
    numer = numer1 * denom2 + numer2 * denom1;
    denom = denom1 * denom2;
    gcd_num = gcd(numer, denom);
    while(gcd_num != 1) {
        numer /= gcd_num;
        denom /= gcd_num;
        gcd_num = gcd(numer, denom);
    }
    answer.push_back(numer);
    answer.push_back(denom);
    return answer;
}