#include <string>
using std::string;
#include <iostream>
using std::cin, std::cout, std::endl;

// sorts A in ascending order in place using Insertion Sort
// precondition:
//    0 <= nA <= declared size of A
void sortAsc(double A[], const int nA) {
   int i = 0;
   while (i < nA - 1) {
      int j = i + 1;
      while (0 != j && A[j - 1] > A[j]) {
         double t = A[j - 1];
         A[j - 1] = A[j];
         A[j] = t;
         j--;
      }
      i++;
   }
}

int main() {
   const int SIZE = 9999;

   char ans = 'y';
   int in;
   while (ans == 'y') {
      cout << "what is the size of the array? ";
      cin >> in;
      double A[SIZE];

      cout << "how many elements are there in the array? ";
      cin >> in;
      int nA = in;
      double e;
      for (int i = 0; i < nA; i++) {
         cout << "what is the " << i << "th element of the array? ";
         cin >> in;
         e = in;
         A[i] = e;
      }

      for (int i = 0; i < nA; i++) {
         cout << A[i] << ' ';
      }
      cout << endl;
      sortAsc(A, nA);
      for (int i = 0; i < nA; i++) {
         cout << A[i] << ' ';
      }
      cout << endl;

      cout << "continue? (y/n) ";
      cin >> ans;
   }

   return 0;
}

