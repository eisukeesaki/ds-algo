#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// return int for given roman numeral
//    precondition:
//       1 <= rn <= 15
//       rn consists of 'I', 'V', 'X', 'L', 'C', 'D', 'M'
//       1 <= rn <= 3999
int roman_to_int(char *rn) {
   char *frmtd = malloc(strlen(rn) * 3 * sizeof(char));
   if (frmtd == NULL) {
      return -1;
   }
   char *frmtd_org = frmtd;

   for (int i = 0; i < strlen(rn); i++) {
      if (rn[i] == 'I' && rn[i + 1] == 'V') {
         *frmtd++ = 'I';
         *frmtd++ = 'I';
         *frmtd++ = 'I';
         *frmtd++ = 'I';
         i++;
      }
      else if (rn[i] == 'I' && rn[i + 1] == 'X') {
         *frmtd++ = 'V';
         *frmtd++ = 'I';
         *frmtd++ = 'I';
         *frmtd++ = 'I';
         *frmtd++ = 'I';
         i++;
      }
      else if (rn[i] == 'X' && rn[i + 1] == 'L') {
         *frmtd++ = 'X';
         *frmtd++ = 'X';
         *frmtd++ = 'X';
         *frmtd++ = 'X';
         i++;
      }
      else if (rn[i] == 'X' && rn[i + 1] == 'C') {
         *frmtd++ = 'L';
         *frmtd++ = 'X';
         *frmtd++ = 'X';
         *frmtd++ = 'X';
         *frmtd++ = 'X';
         i++;
      }
      else if (rn[i] == 'C' && rn[i + 1] == 'D') {
         *frmtd++ = 'C';
         *frmtd++ = 'C';
         *frmtd++ = 'C';
         *frmtd++ = 'C';
         i++;
      }
      else if (rn[i] == 'C' && rn[i + 1] == 'M') {
         *frmtd++ = 'D';
         *frmtd++ = 'C';
         *frmtd++ = 'C';
         *frmtd++ = 'C';
         *frmtd++ = 'C';
         i++;
      }
      else {
         *frmtd++ = rn[i];
      }
   }
   *frmtd++ = '\0';

   int n = 0;
   for (int i = 0; i < strlen(frmtd_org); i++) {
      switch (frmtd_org[i]) {
         case 'I':
            n += 1; break;
         case 'V':
            n += 5; break;
         case 'X':
            n += 10; break;
         case 'L':
            n += 50; break;
         case 'C':
            n += 100; break;
         case 'D':
            n += 500; break;
         case 'M':
            n += 1000; break;
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

