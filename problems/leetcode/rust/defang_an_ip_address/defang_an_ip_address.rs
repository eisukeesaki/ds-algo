// take an ip address and return a defanged version of it
// preconditions:
//    adr is ipv4 address
fn defang_ip_addr(adr: String) -> String {
   let defanged = adr.replace(".", "[.]");
   defanged
}

fn main() {
   let ipv4a = String::from("255.25.2.0");
   let defanged = defang_ip_addr(ipv4a.clone());
   let expected = "255[.]25[.]2[.]0";
   assert_eq!(expected, defanged);
   println!("{ipv4a} {defanged}"); 
}

