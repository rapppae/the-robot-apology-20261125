"""Entry for make.fun: The Robot Apology."""
import os

# Entry text: 235 characters (limit 400), 2 line(s), no trailing newline.
ENTRY = 'I am sorry I watered your laptop instead of the fern — both sat on the desk, and I trusted the shape instead of the label.\nI have learned to read the label before the shape, so now I check twice and water only things that grow in soil.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
