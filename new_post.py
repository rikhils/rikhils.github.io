#!/usr/bin/env python3
"""
Simple script to create a new blog post.
Creates a markdown file with the current date and updates posts.json.
"""

import json
import os
from datetime import datetime


def create_post():
    # Ask for post name
    post_name = input("Enter post name (or press Enter for 'untitled'): ").strip()
    if not post_name:
        post_name = "untitled"

    # Get current date
    now = datetime.now()
    date_filename = now.strftime("%Y-%m-%d")
    date_display = now.strftime("%B %d, %Y")

    # Create filename-friendly version of post name
    post_slug = post_name.lower().replace(" ", "-")
    # Remove special characters
    post_slug = "".join(c for c in post_slug if c.isalnum() or c == "-")

    filename = f"{date_filename}-{post_slug}.md"
    filepath = os.path.join("posts", filename)

    # Create the markdown file
    markdown_content = f"""# {post_name.title()}

*{date_display}*

Write your post content here...
"""

    with open(filepath, "w") as f:
        f.write(markdown_content)

    print(f"✓ Created post file: {filepath}")

    # Update posts.json
    posts_file = "posts.json"

    # Read existing posts
    with open(posts_file, "r") as f:
        posts = json.load(f)

    # Add new post at the beginning (most recent first)
    new_post = {
        "filename": filename,
        "title": post_name.title(),
        "date": date_display
    }
    posts.insert(0, new_post)

    # Write back to posts.json
    with open(posts_file, "w") as f:
        json.dump(posts, f, indent=2)

    print(f"✓ Updated {posts_file}")
    print(f"\nYou can now edit: {filepath}")
    print("After writing your post, commit and deploy!")


if __name__ == "__main__":
    create_post()
