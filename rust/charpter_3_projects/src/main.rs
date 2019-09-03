use std::io;

fn main(){ 
    // 12 days of chrismas
    days_of_christmas();
    

    // fib n
    let fib_n = fib(5);
    println!("fib_n: {}", fib_n);

    // celcius converter
    f_to_c_converter();
    c_to_f_converter();

   
}

fn days_of_christmas() {
    let days = [
        "1st", 
        "2nd", 
        "3rd", 
        "4th", 
        "5th", 
        "6th", 
        "7th", 
        "8th", 
        "9th", 
        "10th", 
        "11th", 
        "12th"
    ];
// would if I could so I should but I wont
    fn day_xmas(day: String) {
        println!("On the {} day of christmas, my true love gave to me", day);
    }
    fn test() {
        println!("would if I could so I should but I wont");
    }

    test();
    for day in days.iter() {
        day_xmas(day.to_string());
    }
}

fn fib(n: u32) -> u32 {
    if n == 0 {
        return 0;
    }else if n == 1 {
        return 1;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}


fn f_to_c_converter() {
    loop {
        println!("Please input temperature (fahrenheight)");
        
        let mut f_temp = String::new();
      
        io::stdin().read_line(&mut f_temp)
            .expect("Failed to read line");

        let f_temp: f32 = match f_temp.trim().parse() {
            Ok(num) => num,
            Err(_) => break,
        };

        let c_temp = (f_temp - 32.0)*(5.0/9.0);
        println!("temp in celcius is {}", c_temp); 
    }
}

fn c_to_f_converter() {
    loop {
        println!("Please input temperature (celcius)");
        
        let mut c_temp = String::new();
      
        io::stdin().read_line(&mut c_temp)
            .expect("Failed to read line");

        let c_temp: f32 = match c_temp.trim().parse() {
            Ok(num) => num,
            Err(_) => break,
        };

        let f_temp = (c_temp)*(9.0/5.0) + 32.0;
        println!("temp in fahrenheight is {}", f_temp);
    }
}
