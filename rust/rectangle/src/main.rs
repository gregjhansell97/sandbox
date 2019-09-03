#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32
}
impl Rectangle {
    // also &mut self
    fn area(self: &Rectangle) -> u32 { // can also be (&self)
        return self.width * self.height;
    }
    fn can_hold(&self, other: &Rectangle) -> bool {
        return self.width > other.width && self.height > other.height;
    }
}
//can have more than one impl location
impl Rectangle {
    fn square(size: u32) -> Rectangle {
        return Rectangle { width: size, height: size };
    }
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };
    println!("{:#?}", rect1);
    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );
    automatic_reference(&rect1);

    let sqr = Rectangle::square(100);
    if sqr.can_hold(&rect1) {
        println!("it can hold");
    }
}

fn automatic_reference(rect: &Rectangle) {
    println!("area: {}", rect.area());
    println!("area: {}", (&rect).area());
}
