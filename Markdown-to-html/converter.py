import markdown
import sys
import os

def convert_md_to_html(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: '{input_path}' does not exist.")
        return

    with open(input_path, 'r', encoding='utf-8') as md_file:
        text = md_file.read()
        html = markdown.markdown(text, extensions=['extra', 'codehilite', 'tables'])

    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html)
    print(f"✅ Converted '{input_path}' to '{output_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input.md> <output.html>")
    else:
        convert_md_to_html(sys.argv[1], sys.argv[2])
