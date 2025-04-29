#include <string.h>
#include <stdlib.h>
#include <stdio.h>

// return sum of differences between all adjacent characters in s
// preconditions:
//    2 <= strlen(s) <= 100
int score_of_string(char *s) {
   int total = 0;
   for (int i = 0; i < strlen(s) - 1; i++) {
      total += abs(s[i] - s[i + 1]);
   }
   return total;
}
int main() {
   // char *s = strdup("ab");
   // int expected = 1;
   char *s = strdup("tgtktpytavhslrnrrxwtbfhqyqronmvlqdxbpsymhgwyb");
   int expected = 374;
   int actual = score_of_string(s);
   if (expected == actual) {
      printf("PASS\n");
   }
   else {
      printf("FAIL\n");
   }
   printf("expected: %d actual: %d \n", expected, actual);
   free(s);
   return 0;
}

