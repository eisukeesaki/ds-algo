// https://leetcode.com/problems/score-of-a-string
//
// Returns the score of s.
// Score is the sum of the absolute difference between ASCII values of adjacent
// characters.
// preconditions:
//    2 <= s.length <= 100
//    s consists of lowercase English exclusively.
fn score_of_string(s: &String) -> i32 {
   let bytes = s.as_bytes();
   let pairs = bytes.windows(2);
   let mut diff;
   let mut sum = 0;
   for pair in pairs {
      if pair[0] > pair[1] {
         diff = pair[0] as i32 - pair[1] as i32;
      }
      else {
         diff = pair[1] as i32 - pair[0] as i32;
      }
      sum += diff;
   }
   sum
}
fn main() {
   // let s = String::from("Alohomora");
   // let s = String::from("hello"); // expect 13
   let s = String::from("tgtktpytavhslrnrrxwtbfhqyqronmvlqdxbpsymhgwyb");
   let abs_diff = score_of_string(&s);
   let expected = 374;
   assert_eq!(abs_diff, expected);
   println!("absolute difference of {s} is {abs_diff}");
}

