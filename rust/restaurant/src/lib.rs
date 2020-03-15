mod front_of_house;

use std::{cmp::Ordering, io};


//hosting is now a valid name in that scope
//idiomatic way to bring a function in is by it's parent module
use crate::front_of_house::hosting;

mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }
    pub enum Appetizer {
        Soup,
        Salad,
    }
    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            } 
        }
    }
    fn fix_incorrect_order() {
        cook_order();
        super::front_of_house::serving::serve_order();
    }
    fn cook_order() {}
}

pub fn eat_at_restaurant() {
    crate::front_of_house::hosting::add_to_waitlist();
    // relative path
    front_of_house::hosting::add_to_waitlist();
    let mut meal = back_of_house::Breakfast::summer("Rye");
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);
    hosting::add_to_waitlist();
}
