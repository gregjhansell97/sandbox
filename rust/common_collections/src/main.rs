fn vector_collection() {
    let mut v_1: Vec<i32> = Vec::new();
    v_1.push(5);
    v_1.push(6);
    let v_2 = vec![1, 2, 3];
    let third: &i32 = &v_2[2];
    let first = &v_1[0];
    v_1.push(10);
    match v_1.get(2) {
        Some(third) => println!("The third element is {}", third),
        None => println!("There is no third element.")
    } 
}

fn main() {
    vector_collection();
    println!("Hello, world!");
}
