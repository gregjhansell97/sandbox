fn main() {
    again();
    break_ret_val();
    while_loop();
    for_loop();
    for_range_loop();
}

fn break_ret_val() {
    let mut counter = 0;
    
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {}", result);
}

fn for_loop() {
    let a = [10, 20, 30, 40, 50];

    for element in a.iter() {
        println!("The value is: {}", element);
    }
}

fn for_range_loop() {
    for number in (1..4).rev() {
        println!("{}!", number);
    }
    println!("LIFTOFF! (for loop style)");
}

fn while_loop() {
    let mut number = 3;
    while number != 0 {
        println!("{}", number);
        number -= 1;
    }
    println!("LIFTOFF!");
}

fn again() {
    loop {
        println!("Again!");
        break;
    }
}
