mod days;

use std::{env, fs};

fn run_day(day: &str, file: &str) {
    let input = fs::read_to_string(format!("inputs/{day}/{file}"))
        .unwrap_or_else(|_| panic!("Missing inputs/{day}/{file}"));

    match day {
        "d00" => {
            println!("Part 1: {}", days::d00::part_01(&input));
            println!("Part 2: {}", days::d00::part_02(&input));
        }
        // [DAYS_MATCH]
        _ => panic!("Unknown day: {day}"),
    }
}

fn main() {
    let day = env::args()
        .nth(1)
        .expect("Specify a day, e.g.: cargo run -- d01");
    run_day(&day, "main.txt");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn d00() {
        run_day("d00", "test.txt");
    }

    // [DAYS_TEST]
}
