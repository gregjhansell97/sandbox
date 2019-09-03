enum IpAddrKind {
    V4(u8, u8, u8, u8),
    V6(String)
}

struct IpAddr {
    kind: IpAddrKind,
    address: String
}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32)
}
impl Message {
    fn call(&self) {
        // method body would be defined here
    }
}

fn main() {
    let home = IpAddr {
        kind: IpAddrKind::V4(127, 0, 0, 1),
        address: String::from("localhost:8080")
    };

    struct Color(u32, u32, u32); // in main method!
    let red = Color(1, 2, 3);

    let four = IpAddrKind::V4(127, 0, 0, 1);
    let six = IpAddrKind::V6(String::from("::1"));
    router(four);
    router(six);


    // use some and none to replace null
    let some_number = Some(5);
    let sum = 5 + some_number;
    // needs option<i32> to infer type of absent number
    let absent_number: Option<i32> = None;
}

fn router(ip_kind: IpAddrKind) {
}
