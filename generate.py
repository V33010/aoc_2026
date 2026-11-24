import re
import sys
from pathlib import Path

DAY_TEMPLATE = """use aoc_2026::*;

pub fn part_01(input: &str) -> usize {
    0
}

pub fn part_02(input: &str) -> usize {
    0
}
"""


def main() -> None:
    if len(sys.argv) != 2 or not re.fullmatch(r"d\d{2}", sys.argv[1]):
        sys.exit("Usage: uv run generate.py d<xx>  (e.g., uv run generate.py d01)")

    day = sys.argv[1]
    root = Path(__file__).parent

    # 1. Create inputs/dxx/test.txt and inputs/dxx/main.txt
    input_dir = root / "inputs" / day
    input_dir.mkdir(parents=True, exist_ok=True)
    for filename in ("test.txt", "main.txt"):
        (input_dir / filename).touch(exist_ok=True)

    # 2. Create src/days/dxx.rs
    days_dir = root / "src" / "days"
    days_dir.mkdir(parents=True, exist_ok=True)
    day_file = days_dir / f"{day}.rs"
    if day_file.exists():
        sys.exit(f"{day_file} already exists.")
    day_file.write_text(DAY_TEMPLATE, encoding="utf-8")

    # 3. Register module in src/days/mod.rs
    mod_file = days_dir / "mod.rs"
    mod_line = f"pub mod {day};\n"
    existing_mods = mod_file.read_text(encoding="utf-8") if mod_file.exists() else ""
    if mod_line not in existing_mods:
        mod_file.write_text(existing_mods + mod_line, encoding="utf-8")

    # 4. Inject match arm and test function into src/main.rs
    main_file = root / "src" / "main.rs"
    main_src = main_file.read_text(encoding="utf-8")

    match_arm = (
        f'        "{day}" => {{\n'
        f'            println!("Part 1: {{}}", days::{day}::part_01(&input));\n'
        f'            println!("Part 2: {{}}", days::{day}::part_02(&input));\n'
        f"        }}\n"
        f"        // [DAYS_MATCH]"
    )
    test_fn = (
        f"    #[test]\n"
        f"    fn {day}() {{\n"
        f'        run_day("{day}", "test.txt");\n'
        f"    }}\n\n"
        f"    // [DAYS_TEST]"
    )

    assert (
        "// [DAYS_MATCH]" in main_src
    ), "Missing // [DAYS_MATCH] marker in src/main.rs"
    assert "// [DAYS_TEST]" in main_src, "Missing // [DAYS_TEST] marker in src/main.rs"

    main_src = main_src.replace("        // [DAYS_MATCH]", match_arm, 1)
    main_src = main_src.replace("    // [DAYS_TEST]", test_fn, 1)
    main_file.write_text(main_src, encoding="utf-8")

    print(f"Scaffolded {day}:")
    print(f"  - src/days/{day}.rs")
    print(f"  - inputs/{day}/test.txt & main.txt")
    print(f"  - Wired into src/days/mod.rs and src/main.rs")


if __name__ == "__main__":
    main()
