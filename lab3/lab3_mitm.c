#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <assert.h>

void encrypt(mpz_t C, const mpz_t M, const unsigned e, const mpz_t n) {
	mpz_powm_ui(C, M, e, n);
}

void MitM (mpz_t res, const mpz_t C, const mpz_t n, const unsigned e) {
	const unsigned lim = 2 << 20; //explicit because I want to save me the
				      //trouble of dynamically allocating
				      //the next array
	mpz_t *X = malloc(lim * sizeof(mpz_t));

	for (int i = 0; i < lim; ++i) {
		mpz_init_set_ui(X[i], i + 1);
		encrypt(X[i], X[i], e, n);
	}
	
	printf("init2\n");
	mpz_t C_S, Se;
	mpz_init(C_S);
	mpz_init(Se);
	for (int i = 0; i < lim; ++i) {
		
		//C_S = C * S^(-e) mod n
		mpz_invert(Se, X[i], n);
		mpz_mul(C_S, C, Se);
		mpz_powm_ui(C_S, C_S, 1, n);
		
		//find a match in X for C_S
		for (int j = 0; j < lim; ++j) {
			if (!mpz_cmp(C_S, X[j])) {
				mpz_set_ui(res, (i + 1) * (j + 1));
				return;
			}
		}
	}

	mpz_clear(C_S);
	mpz_clear(Se);
	for (int i = 0; i < lim; ++i)
		mpz_clear(X[i]);

	//if nothing is found 
	mpz_set_ui(res, 0);
	return;	
}

int main () {
	unsigned e = 65537;
	mpz_t C, n, M;
	mpz_init_set_str(C, "0x860d5c77d6628af7f987355633abb798d3e5d8319314390f378a5bb04c33a728105925be2a98c66044a2eecbf55562d6115635a49b2285a92fd1167d845171ca2ee3c4edb3d3b6259543ba4f41d901c9817d1511c5940df16fad214758a723380fc9866e4d4415233233ab6b41383ec79e20d4bb81e39c5aece6bb61145fc666b17f6daa6b4283a5795b0a0311aa5c96dadf750eb8a65b8510d819f66916e8951740ff12b7e55eadbbf0ebdecc55ff7c238552fc54da98f94382e5e0e99175ef63b8e7e69bb43e460189c74bc9157d1403ea3b9ecd76ed4c5cf0f4848a1ce7d25d36a7c7a74c8a6fc322bc76b02ee005e24232e5a07ff8f12ed0107c2019a8fb", 0);
	
	printf("init0\n");
	mpz_init_set_str(n, "0xF0AAF950A7CDA5CD8BA56C6A4D9281CB30AE1F7365B8596F00140692B02F5997F436039B969B4D2E3C2EF0457DD9AB0D5FD04D40145C799F6627D08CF02288265B47088509C9414B25433631BA9CF79BD668B6E4BC46546857EA6328EBD5FFE85D8DB0DD6E4ED1C1DF5A8D609B79B3E63921EBBCD9F5C8780CD4697FC63251D8E50FA522AAE51040208E3DA8B8C2D2B3A2CC9CBA059A5D3FB3E20A3CAA54E034BFB97CCB3627C665034623A2307B4F0A5079A19DFCB38374173BD260F53FC2FC45299104048B81E408F7F485E00E7D7BB3DCF5A74AC692A942F07B4980050E1F61E4F9FFE84CF62543747C9FFE40ECB4EB72E6976CE97394323FCC03DE9B9A21", 0);
	mpz_init(M);
	printf("init1\n");
	MitM(M, C, n, e);
	
	gmp_printf("Retrieved plaintext: %Zx\n", M);
	
	mpz_clear(C);
	mpz_clear(n);
	mpz_clear(M);

	return 0;
}
