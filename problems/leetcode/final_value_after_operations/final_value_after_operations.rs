// return the result of running increments and decrements on v initialized to 0
// precondition:
//    1 <= ops.len() <= 100
//    increment and decrement ops are one of: "++X", "X++", "--X", or "X--"
fn final_value_after_ops(ops: Vec<String>) -> i32 {
   let mut v = 0;
   for op in ops {
      if op == "--X" || op == "X--" {
         v -= 1;
      }
      else if op == "++X" || op == "X++" {
         v += 1;
      }
   }
   v
}

fn main() {
   let ops: Vec<String> = vec![
      String::from("--X"),
      String::from("++X"),
      String::from("X--"),
      String::from("X++"),
      String::from("X++"),
   ];

   let expected = 1;
   let actual = final_value_after_ops(ops);
   println!("final value {}", actual);
   assert_eq!(expected, actual);
}

