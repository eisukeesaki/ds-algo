//
// returns the sum of the absolute difference between the ASCII values of adjacent characters
what are sliding windows?
fn score_of_string(s: String) -> i32 {
   let bytes = s.as_bytes();
   let mut diff;
   let mut sum = 0;

   // i made an out of bounds error.
   // how could we have made use of rust's functionality to not think about bouds?
   for i in 0..bytes.len() {
      diff = bytes[i] as i32 - bytes[i + 1] as i32;
      sum += diff;
   }
   sum
}

fn main() {
   let s = String::from("hello");
   let score = score_of_string(s);
   assert_eq!(score, 13);
}
//
// fn main() {
//    let s = String::from("hello");
//    for c in s.chars() {
//       println!("{}", c);
//    }
// }
