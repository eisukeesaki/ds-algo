#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// return int for given roman numeral
//    precondition:
//       1 <= rn <= 15
//       rn consists of 'I', 'V', 'X', 'L', 'C', 'D', 'M'
//       1 <= rn <= 3999
int roman_to_int(char *rn) {
   int n = 0;

   for (int i = 0; i < strlen(rn); i++) {
      if (rn[i] == 'I') {
         if (rn[i + 1] == 'V') {
            n += 4;
            i++;
            continue;
         }
         else if (rn[i + 1] == 'X') {
            n += 9;
            i++;
            continue;
         }
         n += 1;
      }
      else if (rn[i] == 'X') {
         if (rn[i + 1] == 'L') {
            n += 40;
            i++;
            continue;
         }
         else if (rn[i + 1] == 'C') {
            n += 90;
            i++;
            continue;
         }
         n += 10;
      }
      else if (rn[i] == 'C') {
         if (rn[i + 1] == 'D') {
            n += 400;
            i++;
            continue;
         }
         else if (rn[i + 1] == 'M') {
            n += 900;
            i++;
            continue;
         }
         n += 100;
      }
      else if (rn[i] == 'V') {
         n += 5;
      }
      else if (rn[i] == 'L') {
         n += 50;
      }
      else if (rn[i] == 'D') {
         n += 500;
      }
      else if (rn[i] == 'M') {
         n += 1000;
      }
   }

   return n;
}

int main() {
   char *rn = "IV";
   int itgr = roman_to_int(rn);
   printf("%s %d\n", rn, itgr);
   return 0;
}

