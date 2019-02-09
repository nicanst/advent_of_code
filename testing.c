#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define LEN 1000000

void clear_array(char *arr) {
  for(int i = 0; i < LEN; i++) {
    arr[i] = '0';
  }
}



int main() {
  char test[LEN];
  clear_array(test);
  test[100] = '1';

  for(int i = 0; i < LEN; i++) {
    if(test[i] != '0') {
      printf("%d",i);
    }
  }

  return 0;

}
