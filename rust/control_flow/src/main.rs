fn main() {
    if_demo();
    if_let_statement(); 
    match_demo();
}

#[derive(Debug)]
enum UsState {
    Alabama,
    Alaska
}
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState)
}
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => { 
            println!("Lucky penny!");
            return 1;
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            return 25;
        }
    }
}
fn match_demo() {
    let c = Coin::Penny;
    let q = Coin::Quarter(UsState::Alaska);
    println!("{}", value_in_cents(c));
    println!("{}", value_in_cents(q));
    let five = Some(5);
    match five {
        Some(i) => {
            println!("{}", i);
        },
        None => {
            println!("No dice");
        }
    }
    if let Some(5) = five {
        println!("here?");
    }
    if let Some(i) = five {
        println!("{}", i);
    }
// _ => { matches all not specified before it
}

fn if_demo() {
    let bool_val = true;
    if bool_val { // must be a boolean not a number
        println!("condition was true");
    } else {
        println!("condition was false");
    }


    let number = 6;

    // matching would be better for refactoring
    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}

fn if_let_statement() {
    let condition = true;
    let number = if condition {
        5
    } else {
        6
    };

    println!("The value of number is: {}", number);
}
