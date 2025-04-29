#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// return an array of indices of words containing x
// preconditions:
//    1 <= words.len(), words[i].len() <= 50
//    x is a lowercase English letter
//    words[i] consists of lowercase English letters exclusively
int *find_words_containing(char **words, int words_size, char x, int *return_size) {
   int *containing = malloc(words_size * sizeof(int));
   if (containing == NULL) {
      return NULL;
   }

   *return_size = 0;

   for (int i = 0; i < words_size; i++) {
      if (strchr(words[i], x) != NULL) {
         containing[*return_size] = i;
         (*return_size)++;
      }
   }

   return containing;
}

int main() {
   int actual_n_containing = 0;

   // char *words[] = {"abc","bcd","aaaa","cbc"};
   // const int words_size = 4;
   // char x = 'a';

   char *words[] = {"leet","code"};
   const int words_size = 2;
   char x = 'e';

   int *actual_containing = 
      find_words_containing(words, words_size, x, &actual_n_containing);
   int expected_containing[] = {0, 1};
   const int expected_n_containing = 2;
   if (expected_n_containing == actual_n_containing) {
      for (int i = 0; i < expected_n_containing; i++) {
         printf("%d\n", actual_containing[i]);
         if (actual_containing[i] != expected_containing[i]) {
            printf("FAIL\nindices doesn't match");
            return 1;
         }
      }
      printf("PASS\n");
      return 0;
   }
   printf("FAIL\nactual_containing != expected_containing");

   free(actual_containing);

   return 1;
}

