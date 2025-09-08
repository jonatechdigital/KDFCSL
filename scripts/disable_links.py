import os

# --- Configuration ---
# The folder where your HTML files are. "." means the current folder.
html_folder = "."
# The class to add to the links.
class_to_add = "is-disabled"
# The specific class of the social links we want to target.
target_link_class = "social-icons2_link"
# --- End of Configuration ---

def process_html_file(file_path):
    """Reads an HTML file, adds the class to the specified links, and saves it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # What to find: a link with the target class that doesn't already have the disabled class.
        find_str = f'class="{target_link_class} w-inline-block"'
        # What to replace it with:
        replace_str = f'class="{target_link_class} w-inline-block {class_to_add}"'

        if find_str in content:
            new_content = content.replace(find_str, replace_str)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated: {file_path}")
        else:
            print(f"⚪️ No changes needed for: {file_path}")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def main():
    """Finds all HTML files in the specified folder and processes them."""
    print("Starting update process...")
    for filename in os.listdir(html_folder):
        if filename.endswith(".html"):
            process_html_file(os.path.join(html_folder, filename))
    print("\nUpdate process complete!")

if __name__ == "__main__":
    main()