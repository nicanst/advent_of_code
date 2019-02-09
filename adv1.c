#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define ARRAY_LEN 15

// void make_to_int(char *arr) {
//   // putchar(arr[0]);
//   int ten = 0;
//   int number = 0;
//   // if(arr[0] == '+') {
//   //   number = atoi(%test[1]);
//   // }
//   // else if (arr[0] == '-') {
//   //   number = atoi(%test[1]) * -1;
//   // }
//   //   printf("%d",number);
//   // return 1;
// }

void clear_array(char *arr) {
  for(int i = 0; i < ARRAY_LEN; i++) {
    arr[i] = '\0';
  }
}

int main() {
  FILE *fp;
  char input_char;
  char input_row[ARRAY_LEN];
  clear_array(input_row);
  int answer = 0;
  int i = 0;

  fp = fopen("adv1.txt", "r");
  if (fp == NULL) {
    perror("Går inte att öppna fil\n");
    return -1;
  } else {
    while((input_char = fgetc(fp)) != EOF) {
      if (!(input_char == '\n') && !(input_char == EOF)) {
        input_row[i] = input_char;
      } else {
        answer += atoi(input_row);
        i = -1;
        clear_array(input_row);
      }
      i++;
    }
  }
  printf("%d", answer);
  putchar('\n');
  fclose(fp);
  return 0;

}
