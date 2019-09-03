fn main() {
    variable_scope(); 
    invalid_s1();
    ownership_changes();

    let mut s = String::from("hello");
//    let r1 = &mut s; only one mutable borrow
//    let r2 = &mut s;
//    println!("{}, {}, r1, r2");

    change(&mut s);
    change(&mut s);
    println!("{}", s);
}

fn variable_scope() {
    let mut s = String::from("hello"); // allocated on the heap (not stack)
    s.push_str(", world!");
    println!("{}", s);
}

fn invalid_s1() {
    let s1 = String::from("s1");
    let s2 = s1.clone();

    println!("{}, world!", s1);
}

fn ownership_changes() {
    let s = String::from("hello");

    takes_ownership(s); // s's value moves into the function (no longer valid here)
    //takes_ownership(s);

    let x = 5;  // x comes into scope

    makes_copy(x); // x would move into the function. but i32 is Copy, so its okay

    let z = gives_ownership();
}

fn takes_ownership(some_string: String) {
    println!("{}", some_string);
} // some_string goes out of scope and "drop" is called. the backing memory is free

fn makes_copy(some_integer: i32) {
    println!("{}", some_integer);
} // here, some_integer goes out of scope. Nothing special happens.

fn gives_ownership() -> String {
    let some_string = String::from("hello");
    return some_string; // some string is returned out to the calling function
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
