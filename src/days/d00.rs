#![allow(unused)]
use aoc_2026::*;

pub fn part_01(input: &str) -> usize {
    let parsed_input = parse_input(input);
    let mut value: i32 = 50;
    let mut counter = 0;
    for item in parsed_input {
        // println!("item: {item}");
        let extracted: i32 = item[1..].parse().expect("unable to parse.");
        // println!("extracted: {extracted}");
        let direction: &str = &item[..1];
        // println!("direction: {direction}");
        value = match direction {
            "L" => {
                let new = (value - extracted) % 100;
                if new >= 0 { new } else { 100 + new }
            }
            "R" => {
                let temp = value;

                (temp + extracted) % 100
            }
            _ => panic!("Unknown direction: {direction}"),
        };
        if value == 0 {
            counter += 1;
        }
    }

    counter
}

pub fn part_02(input: &str) -> usize {
    let parsed_input = parse_input(input);
    let mut value: i32 = 50;
    let mut counter = 0;
    for item in parsed_input {
        println!("item: {item}");
        let extracted: i32 = item[1..].parse().expect("unable to parse.");
        println!("extracted: {extracted}");
        let direction: &str = &item[..1];
        println!("direction: {direction}");
        value = match direction {
            "L" => {
                let dist_to_first_zero = if value == 0 { 100 } else { value };
                if extracted >= dist_to_first_zero {
                    counter += (1 + (extracted - dist_to_first_zero) / 100) as usize;
                }
                (value - extracted).rem_euclid(100)
            }
            "R" => {
                let temp = value;
                counter += ((temp + extracted) / 100) as usize;

                (temp + extracted) % 100
            }
            _ => panic!("Unknown direction: {direction}"),
        };
    }

    counter
}
