import os
import re

# --- Configuration ---
html_folder = "."
final_css_file = "css/main.min.css"
# --- End of Configuration ---


def process_html_file(file_path):
    """Reads an HTML file, replaces the CSS links, and saves it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find the block of three CSS link tags.
        css_block_pattern = re.compile(
            r'<link href="css/normalize.css".*?>\s*'
            r'<link href="css/webflow.css".*?>\s*'
            r'<link href="css/kimwanyidiaryfarmers-draft.webflow.css".*?>',
            re.DOTALL
        )

        # The new single link tag to replace the block with.
        replacement_str = f'<link href="{final_css_file}" rel="stylesheet" type="text/css">'

        if css_block_pattern.search(content):
            new_content = css_block_pattern.sub(replacement_str, content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated CSS links in: {file_path}")
        else:
            print(
                f"⚪️ No changes needed for: {file_path} (already updated or block not found)")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")


def main():
    """Finds all HTML files and processes them."""
    print("Starting to update CSS links for publishing...")
    for filename in os.listdir(html_folder):
        if filename.endswith(".html"):
            process_html_file(os.path.join(html_folder, filename))
    print("\nCSS link update complete! Your site is ready to publish.")


if __name__ == "__main__":
    main()
