#include <string.h>
#include <stdio.h>

does source code of linux kernel use break statements?
// return number of jewels in stones where:
// jewels are represented as case-sentive characters in jewels and
// stones are jewels if they appear in jewels
// preconditions:
//    1 <= jewels.len(), stones.len() <= 50
int num_jewels_in_stones(char* jewels, char* stones) {
   int jewels_in_stones = 0;
   int n_jewels = strlen(jewels);
   int n_stones = strlen(stones);
   for (int i = 0; i < n_stones; i++) {
      for (int j = 0; j < n_jewels; j++) {
         if (stones[i] == jewels[j]) {
            jewels_in_stones++;
            break;
         }
      }
   }
   return jewels_in_stones;
}

int main() {
   char *j = strdup("aA");
   char *s = strdup("aAAbbbb");
   int expected_n = 3;
   int actual_n = num_jewels_in_stones(j, s);
   if (expected_n == actual_n) {
      printf("PASS\n");
   }
   else {
      printf("FAIL\n");
   }
   return 0;
}

