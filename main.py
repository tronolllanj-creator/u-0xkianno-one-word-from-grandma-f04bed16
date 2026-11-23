# Write the word 'witchcraft' with a trailing newline to /output/entry.txt
# Gate: entry.txt must be 1-30 chars, word plus one newline only.
import os

WORD = "witchcraft"


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "entry.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
