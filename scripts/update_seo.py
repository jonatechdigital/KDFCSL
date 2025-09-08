import os
import re

# --- SEO Configuration ---
# Define the titles and descriptions for each page.
# You can easily change these values whenever you want.
page_seo_data = {
    "index.html": {
        "title": "KDFCSL | Transforming Nakaseke's Dairy Farmers",
        "description": "For over 50 years, Kimwanyi Dairy Farmers' Cooperative Society (KDFCSL) has been uplifting vulnerable communities in Nakaseke, Uganda through sustainable agriculture."
    },
    "about-us.html": {
        "title": "About Us | KDFCSL",
        "description": "Learn about the 50+ year history of KDFCSL and our mission to empower women, youth, and the elderly in Nakaseke through community-driven agricultural programs."
    },
    "impact.html": {
        "title": "Our Impact | KDFCSL",
        "description": "Discover the real-life impact of our work, from empowering women-led enterprises to improving community health and enabling children to attend school."
    },
    "partner-with-us.html": {
        "title": "Partner With Us | KDFCSL",
        "description": "Join KDFCSL in our mission. Partner with us to contribute to a brighter, sustainable future for vulnerable farming communities in Nakaseke, Uganda."
    },
    "form.html": {
        "title": "Contact Us | KDFCSL",
        "description": "Get in touch with the Kimwanyi Dairy Farmers' Cooperative Society. We'd love to hear from you and explore potential partnerships."
    }
    # Add other HTML files here if they need unique titles/descriptions.
    # e.g., "404.html": { "title": "Page Not Found | KDFCSL", "description": "..." }
}
# --- End of Configuration ---


def update_html_file(file_path, seo):
    """Updates the title and meta description of an HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Title
        new_title = f"<title>{seo['title']}</title>"
        content = re.sub(r'<title>.*?</title>', new_title, content, count=1)

        # Update or Add Meta Description
        meta_description_tag = f'<meta content="{seo["description"]}" name="description">'
        
        # Check if a meta description tag already exists
        if re.search(r'<meta content=".*?" name="description">', content):
            content = re.sub(r'<meta content=".*?" name="description">', meta_description_tag, content, count=1)
        else:
            # If not, add it right after the title tag
            content = content.replace('</title>', f'</title>\n  {meta_description_tag}')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated SEO for: {file_path}")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def main():
    """Finds and processes all relevant HTML files."""
    print("Starting SEO update...")
    for filename, seo_data in page_seo_data.items():
        file_path = os.path.join(os.getcwd(), filename)
        if os.path.exists(file_path):
            update_html_file(file_path, seo_data)
        else:
            print(f"⚪️ File not found, skipping: {filename}")
    print("\nSEO update complete!")


if __name__ == "__main__":
    main()