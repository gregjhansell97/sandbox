fn main() {
    println!("Hello, world!");

    another_function(5, 7);

    let y = {
        let x = 3;
        x + 1 // no semi-colon makes it an expression (not a statement)
    };

    println!("The value of y is {}", y);

    println!("The value of five() is {}", five());
}


// functions can be statements or expressions
// statements do not return a value, expressions do

// provide type defintions in parameters
fn another_function(x: i32, y: i32) {
    println!("The value of x is: {}", x);
    println!("The value of y is: {}", y);
}

fn five() -> i32 {
    5 // 5, return 5 or return 5; all work, but 5; does not
}
