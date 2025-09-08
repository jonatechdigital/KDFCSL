import os
import re

# --- Configuration ---
html_folder = "."
jquery_script_tag = '<script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js'
webflow_script_tag = '<script src="js/webflow.js'
# --- End of Configuration ---


def process_html_file(file_path):
    """Reads an HTML file and adds the defer attribute to script tags."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        made_change = False
        # Defer jQuery
        if jquery_script_tag in content and ' defer' not in content:
            content = content.replace(
                jquery_script_tag, jquery_script_tag + '" defer')
            made_change = True

        # Defer webflow.js
        if webflow_script_tag in content and ' defer' not in content:
            content = content.replace(
                webflow_script_tag, webflow_script_tag + '" defer')
            made_change = True

        if made_change:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Added 'defer' to scripts in: {file_path}")
        else:
            print(f"⚪️ No changes needed for: {file_path}")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")


def main():
    """Finds all HTML files and processes them."""
    print("Starting to add 'defer' to script tags...")
    for filename in os.listdir(html_folder):
        if filename.endswith(".html"):
            process_html_file(os.path.join(html_folder, filename))
    print("\nScript defer update complete!")


if __name__ == "__main__":
    main()
