#include<bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(k);
    for (int &i: a) cin >> i;
    vector<int> pre(k + 1), suf(k + 1);
    for (int i = 1; i <= k; i++) {
        pre[i] = pre[i - 1];
        if (i % 2 == 0) pre[i] += a[i - 1] - a[i - 2];
        cout << pre[i];
    }
    for (int i = k - 1; i >= 0; i--) {
        suf[i] = suf[i + 1];
        if ((k - i) % 2 == 0) suf[i] += a[i + 1] - a[i];
    }
    
    int ans = 1e9;
    for (int i = 0; i <= k; i += 2) {
        ans = min(ans, pre[i] + suf[i]);
    }
    // cout << ans << endl;
}
