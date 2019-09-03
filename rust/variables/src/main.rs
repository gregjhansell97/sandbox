fn main() {

// mutability
    /*
        let mut x = 5;
        println!("The value of x is: {}", x);
        x = 6;
        println!("The value of x is: {}", x);
    */

// constants
    //const MAX_POINTS: u32 = 100_000;


// shadowing
    /*
    let x = 5;
    let x = x + 1;
    let x = x + 2;
    let x = "     ";
    */

    /* y keeps its type: this will be an error
    let mut y = 10;
    y = "     ";
    */

    //println!("The value of x is: {}", x);


// tuple
    //let tup: (i32, f64, u8) = (500, 6.4, 1);
    //const FIB_BASE: (i32, i32, i32) = (0, 1, 1);

    //let (x, y, z) = tup;
    //println!("{}-{}-{}", x, y, z);
    //println!("{}", FIB_BASE.1);

// array
    let a = [1, 2, 3, 4]; // data is allocated on stack (not heap)
    let b: [i32; 3] = [1, 2, 3];
    // let a = [3; 5] //(which is [3, 3, 3, 3, 3]
    let first = a[0];
    let second = b[2];

    let out_of_bounds_index = 100;
    let out_of_bounds = a[out_of_bounds_index];

    println!("{}-{}-{}", first, second, out_of_bounds);

}
