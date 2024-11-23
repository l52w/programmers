#include <stdio.h>
#include <string.h>
#include <math.h>

int main() {
	int n, ans = 0;
	char s[1000];
	scanf("%s %d", s, &n);

	int len = strlen(s);
	for (int i = len - 1; i >= 0; i--) { 
		if ('A' <= s[i] && s[i] <= 'Z') {
			ans += pow(n, len - i - 1)*(s[i] - 'A' + 10);
		} else ans += pow(n, len - i - 1)*(s[i] - '0');
	}
	printf("%d", ans);
}