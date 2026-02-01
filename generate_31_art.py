#!/usr/bin/env python3
"""
GitHub Contribution Graph Art Generator ("31")
GitHub 貢獻牆藝術繪圖器 ("31")

Generates a series of git commits with custom GIT_AUTHOR_DATE to render
the digits "31" on the GitHub contribution calendar graph.
"""

import argparse
import datetime
import subprocess
import sys

# 7 rows (Sunday=0 to Saturday=6), 5 columns per digit
# 1 = active commit pixel (dark green), 0 = empty pixel
DIGIT_3 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

DIGIT_1 = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0]
]

def render_matrix_ascii(matrix, title="Matrix"):
    print(f"=== {title} ===")
    for row in matrix:
        print("".join(["██" if pixel else "  " for pixel in row]))
    print()

def get_sunday_start_date(weeks_ago=50):
    today = datetime.date.today()
    # Find last Sunday 'weeks_ago' weeks ago
    idx = (today.weekday() + 1) % 7 # 0=Sunday, 1=Monday...
    last_sunday = today - datetime.timedelta(days=idx)
    start_sunday = last_sunday - datetime.timedelta(weeks=weeks_ago)
    return start_sunday

def main():
    parser = argparse.ArgumentParser(description="Generate GitHub Contribution Graph Art '31'")
    parser.add_argument("--dry-run", action="store_true", help="Print matrix and planned commits without committing")
    parser.add_argument("--commits-per-pixel", type=int, default=10, help="Number of commits per pixel for deep green color (default: 10)")
    parser.add_argument("--week-offset-3", type=int, default=18, help="Starting week offset for digit '3' (0-52)")
    parser.add_argument("--week-offset-1", type=int, default=26, help="Starting week offset for digit '1' (0-52)")
    args = parser.parse_args()

    print("=== GitHub Paint / Art: '31' Generator ===")
    render_matrix_ascii(DIGIT_3, "Digit 3 Pattern")
    render_matrix_ascii(DIGIT_1, "Digit 1 Pattern")

    start_sunday = get_sunday_start_date(50)
    print(f"Grid Start Date (Sunday): {start_sunday}")

    commit_targets = [] # List of (date_str, count)

    # Calculate dates for Digit '3'
    for col_idx in range(5):
        week_num = args.week_offset_3 + col_idx
        for row_idx in range(7):
            if DIGIT_3[row_idx][col_idx]:
                pixel_date = start_sunday + datetime.timedelta(weeks=week_num, days=row_idx)
                commit_targets.append((pixel_date, args.commits_per_pixel))

    # Calculate dates for Digit '1'
    for col_idx in range(5):
        week_num = args.week_offset_1 + col_idx
        for row_idx in range(7):
            if DIGIT_1[row_idx][col_idx]:
                pixel_date = start_sunday + datetime.timedelta(weeks=week_num, days=row_idx)
                commit_targets.append((pixel_date, args.commits_per_pixel))

    print(f"Total active pixel dates: {len(commit_targets)}")
    print(f"Total planned commits: {len(commit_targets) * args.commits_per_pixel}")

    if args.dry_run:
        print("\n[DRY RUN MODE] Listing first 10 target dates:")
        for dt, count in commit_targets[:10]:
            print(f"  Date: {dt} -> {count} commits")
        print("Dry run completed. No git commits created.")
        return

    # Create dummy art log file
    art_file = "art_history.log"
    total_done = 0
    for dt, count in commit_targets:
        date_iso = f"{dt}T12:00:00"
        for i in range(count):
            with open(art_file, "a") as f:
                f.write(f"Contribution pixel 31 date={date_iso} commit={i+1}\n")
            
            subprocess.run(["git", "add", art_file], check=True)
            env = {
                "GIT_AUTHOR_DATE": date_iso,
                "GIT_COMMITTER_DATE": date_iso
            }
            subprocess.run(
                ["git", "commit", "-m", f"Art 31 pixel commit for {dt} ({i+1}/{count})"],
                env={**subprocess.os.environ, **env},
                check=True,
                stdout=subprocess.DEVNULL
            )
            total_done += 1

    print(f"\n[SUCCESS] Successfully generated {total_done} spoofed commits for GitHub Art '31'!")

if __name__ == "__main__":
    main()
