#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define SET_LEN 1000000
#define INT_LEN 1000
#define CH_ARR_LEN 15

void clear_array(char *arr, int arr_len) {
  for(int i = 0; i < arr_len; i++) {
    arr[i] = '\0';
  }
}

int main() {
  FILE *fp;
  int input_numbers[INT_LEN];
  char set_pos[SET_LEN];
  char set_neg[SET_LEN];
  int i = 0;
  char ch;
  char ch_arr[CH_ARR_LEN];
  int answer = 0;
  int ii = 0;

  for(int x = 0; x < SET_LEN; x++) {
    set_pos[x] = '0';
    set_neg[x] = '0';
  }

  for(int y = 0; y < INT_LEN; y++) {
    input_numbers[y] = 0;
  }

  fp = fopen("adv1.txt", "r");
  if (fp == NULL) {
    perror("Går inte att öppna fil\n");
    return -1;
  } else {
    i = 0;
    while((ch = fgetc(fp)) != EOF) {
      if (!(ch == '\n') && !(ch == EOF)) {
        ch_arr[i] = ch;
      } else {
        input_numbers[ii] = atoi(ch_arr);
        // printf(" --%d-- ",ii);
        i = -1;
        clear_array(ch_arr,CH_ARR_LEN);
        ii++;
      }
      i++;
    }
  }

  // for(int y = 0; y < INT_LEN; y++) {
  //   printf("%d: %d\n", y, input_numbers[y]);
  // }

  // char set_pos[SET_LEN];
  // char set_neg[SET_LEN];
  int fortsatt = 1;
  int check = 0;
  int summan = 0;
  int svarstalet = 0;

  //
  //
  //
  while (fortsatt == 1)
  {
    for(int y = 0; y < INT_LEN; y++)
    {
      summan += input_numbers[y];

      if (summan > 0)
      {
        if (set_pos[summan] == '1')
        {
          printf("Talet %d.\n", summan);
          fortsatt = 0;
          break;
        }
        else
        {
          set_pos[summan] = '1';
        }
      }
      else if (summan < 0)
      {
        if(set_neg[-1 * summan] == '1')
        {
          printf("Talet %d.\n", summan);
          fortsatt = 0;
          break;
        }
        else
        {
          set_neg[-1 * summan] = '1';
        }
      }
      else
      {
        printf("Talet  0.\n");
        fortsatt = 0;
        break;
      }
      check++;
      // printf("%d",set_neg[40]);
      printf("%d: f%d in%d su%d neg%c pos%c\n", y, fortsatt, input_numbers[y], summan, set_neg[summan * -1], set_pos[summan]);

    } //for

    check++;
    if(check > 500000) {
      fortsatt = 0;
    }
  } //while

  printf("test");
  fclose(fp);
  return 0;

}
