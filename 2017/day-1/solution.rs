use std::fs::File;
use std::io::{self, BufReader, Read};

fn part_1(buffer: &str) -> u32 {
    let mut total = 0;
    let mut first_char = None;
    let mut prev_char = None;

    for (i, c) in buffer.chars().enumerate() {
        if i == 0 {
            first_char = Some(c);
        }

        if let Some(prev) = prev_char {
            if prev == c {
                total += c as u32 - 48;
            }
        }

        if c.is_numeric() {
            prev_char = Some(c);
        } else {
            break;
        }
    }

    if let Some(first) = first_char {
        if first == prev_char.unwrap() {
            total += first as u32 - 48;
        }
    }

    total
}

fn part_2(buffer: &str) -> u32 {
    let numbers: Vec<u32> = buffer
        .chars()
        .filter(|c| c.is_numeric())
        .map(|c| c as u32 - 48)
        .collect();

    let middle = numbers.len() / 2;
    let mut total = 0;

    for (i, c) in numbers.iter().enumerate() {
        if *c == numbers[(middle + i) % numbers.len()] {
            total += c;
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

