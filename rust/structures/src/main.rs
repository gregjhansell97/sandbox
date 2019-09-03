// storing references in structs require life times (not covered yet)
struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool
}

// unnamed values
struct Color(i32, i32, i32);

fn main() {
    println!("Hello, world!");
    let user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1
    };
    // entire structure must be marked as mutable
    // ..user1 is update syntax
    let mut user2 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        ..user1
    };
    user2.email = String::from("anotheremail@example.com");
    println!("{}", user1.email);
    println!("{}", user2.username);
    println!("{}", user1.active);
    println!("{}", user2.sign_in_count);
    
    let black = Color(0, 12, 22);
    println!("{}", black.1);
   
}

fn build_user(email: String, username: String) -> User {
    return User {
        email, 
        username,
        active: true,
        sign_in_count: 1
    };
}
