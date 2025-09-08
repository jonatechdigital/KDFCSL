import os
import re

# --- Configuration ---
# The folder where your HTML files are. "." means the current folder.
html_folder = "."
# The specific inline style we want to remove.
style_to_remove = 'style="opacity:0"'
# --- End of Configuration ---

def process_html_file(file_path):
    """Reads an HTML file, removes the specified inline style, and saves it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # We add a space before the style attribute to avoid accidentally
        # matching it as part of another word.
        find_str = f' {style_to_remove}'

        if find_str in content:
            # Replace the found string with an empty string to remove it.
            new_content = content.replace(find_str, '')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Cleaned up inline styles in: {file_path}")
        else:
            print(f"⚪️ No inline styles to clean in: {file_path}")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def main():
    """Finds all HTML files and processes them."""
    print("Starting inline style cleanup...")
    for filename in os.listdir(html_folder):
        if filename.endswith(".html"):
            process_html_file(os.path.join(html_folder, filename))
    print("\nCleanup complete!")

if __name__ == "__main__":
    main()