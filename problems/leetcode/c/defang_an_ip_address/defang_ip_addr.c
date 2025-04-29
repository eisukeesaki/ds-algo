#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// take an ip address and return a defanged version of it
// preconditions:
//    adr is ipv4 address
// time to complete grows linearly with respect to input size
// space required grows linearly with respect to input size
char *defangIPaddr(char *address) {
   char *defanged = malloc(strlen(address) + (strlen("[.]") * 3) + 1);
   if (defanged == NULL) {
      return NULL;
   }
   int j = 0;

   for (int i = 0; address[i] != '\0'; i++) {
      if (address[i] == '.') {
         defanged[j++] = '[';
         defanged[j++] = '.';
         defanged[j++] = ']';
      }
      else {
         defanged[j++] = address[i];
      }
   }
   defanged[j] = '\0';

   return defanged;
}

int main() {
   char a[15] = "255.25.2.0";
   char expected[17] = "255[.]25[.]2[.]0";
   // char a[15] = "255.255.255.255";
   // char expected[22] = "255[.]255[.]255[.]255";

   char *d = defangIPaddr(a);

   printf("%s\n", d);
   if (strcmp(expected, d) == 0) {
      printf("PASS\n");
   }
   else {
      printf("FAIL\n");
   };

   free(d);

   return 0;
}

