#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int strStr(char* haystack, char* needle) {
	if (haystack == NULL || needle == NULL) 
		return -1;

	const int len_h = strlen(haystack);
	const int len_n = strlen(needle);
	for (int i = 0; i < len_h - len_n + 1; i++){
		int j = 0;
		for (; j < len_n; j++){
			if (haystack[i+j] != needle[j]){
				break;
			}
		}
		if (j == len_n) return i;
	}

	return -1;
	
}

int main(int argc, char** argv ){
	printf("result = %d\n",strStr("source","urc"));
}
