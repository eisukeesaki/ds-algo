// return number of jewels in stones where:
// jewels are represented as case-sentive characters in jewels and
// stones are jewels if they appear in jewels
// preconditions:
//    1 <= jewels.len(), stones.len() <= 50
fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
   let mut tot_jewels = 0;
   for stone in stones.chars() {
      if jewels.contains(stone) {
         tot_jewels += 1;
      }
   }
   tot_jewels
}

fn main() {
   let s = String::from("aAAbbbb");
   let j = String::from("aA");
   let actual_n = num_jewels_in_stones(j, s);
   let expected_n = 3;
   assert_eq!(expected_n, actual_n);
}

