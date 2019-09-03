fn main() {
    tricky();
    let mut s1 = String::from("hello");
    let len = calculate_length(&s1);

    //let z = &mut s1; (only one per scope)
    change(&mut s1);

    one_per_scope();

    //println!("useless z {}", z);

    println!("The length of '{}' is {}", s1, len);
}

// multiple mutable references
fn one_per_scope() {
    let mut s = String::from("hello");

    { // scope change fixes mutability (only one per scope)
        let r1 = &mut s;
        println!("{}", r1);
    }
    let r2 = &mut s;

    println!("{}", r2);
}

fn calculate_length(s: &String) -> usize {
   // s.push_str(", world"); // cannot modify s
    return s.len();
} // here s goes out of scope but because it does not have ownership of 
// what it refers to, nothing happens.


fn change(some_string: &mut String) {
    some_string.push_str(", world");
}

fn trick() {
    let mut s = String::from("hello");

    let r1 = &s;
    let r2 = &s; 
    println("{} and {}", r1, r2);
    // r1 and r2 are no longe rused after this point

    let r3 = &mut s;
    println!("{}", r3);
}
