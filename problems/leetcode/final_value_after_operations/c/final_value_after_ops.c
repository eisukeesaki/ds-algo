#include <stdio.h>
#include <string.h>

// return the result of running increments and decrements on total initialized
// to 0
// precondition:
//    1 <= ops.len() <= 100
//    increment and decrement ops are one of: "++X", "X++", "--X", or "X--"
int final_value_after_ops(char **ops, int ops_size) {
   int total = 0;
   for (int i = 0; i < ops_size; i++) {
      if (strcmp(ops[i], "--X") == 0 || strcmp(ops[i], "X--") == 0) {
         total--;
      }
      else if (strcmp(ops[i], "++X") == 0 || strcmp(ops[i], "X++") == 0) {
         total++;
      }
   }
   return total;
}

int main() {
   const int ops_size = 5;
   char *ops[] = {
      "--X",
      "++X",
      "X--",
      "X++",
      "X++",
   };
   int actual = final_value_after_ops(ops, ops_size);
   int expected = 1;
   printf("final value %d\n", actual);
   if (actual == expected) {
      printf("PASS\n");
   }
   else {
      printf("FAIL\n");
   }
   return 0;
}

