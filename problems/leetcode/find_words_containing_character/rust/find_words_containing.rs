// return an array of indices of words containing x
// preconditions:
//    1 <= words.len(), words[i].len() <= 50
//    x is a lowercase English letter
//    words[i] consists of lowercase English letters exclusively
fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
   let mut containing: Vec<i32> = Vec::new();
   for (i, word) in words.iter().enumerate() {
      if word.contains(x) {
         containing.push(i as i32);
      }
   }
   containing
}

fn main() {
   let words: Vec<String> = vec![
      String::from("abc"),
      String::from("bcd"),
      String::from("aaaa"),
      String::from("cbc"),
   ];
   let x = 'a';
   let actual_containing = find_words_containing(words, x);
   let expected_containing: Vec<i32> = vec![0, 2];
   assert_eq!(expected_containing, actual_containing);
}

