use std::fs::File;
use std::io::{self, BufReader, Read};

fn part_1(buffer: &str) -> i32 {
    let mut total = 0;
    for line in buffer.lines() {
        let nums: Vec<i32> = line.split("\t").map(|x| x.parse().unwrap()).collect();
        let min = nums.iter().min().unwrap();
        let max = nums.iter().max().unwrap();
        total += max - min;
    }
    total
}

fn part_2(buffer: &str) -> i32 {
    let mut total = 0;
    for line in buffer.lines() {
        let nums: Vec<i32> = line.split("\t").map(|x| x.parse().unwrap()).collect();
        for i in 0..nums.len() {
            for j in 0..nums.len() {
                if i == j {
                    continue;
                }
                if nums[i] % nums[j] == 0 {
                    total += nums[i] / nums[j];
                }
            }
        }
    }
    total
}

fn main() -> io::Result<()> {
    // Open the file for reading
    let file = File::open("input.txt")?;
    let mut reader = BufReader::new(file);

    // Read the entire file into the buffer
    let mut buffer = String::new();
    reader.read_to_string(&mut buffer)?;

    // Call part_1 and part_2 functions
    let total_part_1 = part_1(&buffer);
    let total_part_2 = part_2(&buffer);

    // Print the results
    println!("Total part 1: {}", total_part_1);
    println!("Total part 2: {}", total_part_2);

    Ok(())
}
