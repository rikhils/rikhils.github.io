#!/usr/bin/env python3

import json
import os
from pathlib import Path

def load_posts():
    """Load posts from posts.json"""
    try:
        with open('posts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: posts.json file not found")
        return []
    except json.JSONDecodeError:
        print("Error: posts.json is not valid JSON")
        return []

def save_posts(posts):
    """Save posts to posts.json"""
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)

def delete_post_file(filename):
    """Delete the post markdown file"""
    post_path = Path('posts') / filename
    if post_path.exists():
        post_path.unlink()
        return True
    return False

def display_posts(posts):
    """Display all posts with numbering"""
    print("\n=== Available Posts ===\n")
    for idx, post in enumerate(posts, 1):
        print(f"{idx}. {post['title']}")
        print(f"   Date: {post['date']}")
        print(f"   File: {post['filename']}")
        print()

def main():
    # Load posts
    posts = load_posts()

    if not posts:
        print("No posts found to delete.")
        return

    # Display posts
    display_posts(posts)

    # Get user selection
    try:
        choice = input("Enter the number of the post to delete (or 'q' to quit): ").strip()

        if choice.lower() == 'q':
            print("Cancelled.")
            return

        post_number = int(choice)

        if post_number < 1 or post_number > len(posts):
            print(f"Error: Please enter a number between 1 and {len(posts)}")
            return

        # Get the selected post (adjust for 0-indexing)
        selected_post = posts[post_number - 1]

        # Confirm deletion
        confirm = input(f"\nAre you sure you want to delete '{selected_post['title']}'? (yes/no): ").strip().lower()

        if confirm != 'yes':
            print("Cancelled.")
            return

        # Delete the markdown file
        if delete_post_file(selected_post['filename']):
            print(f"✓ Deleted file: posts/{selected_post['filename']}")
        else:
            print(f"⚠ Warning: File posts/{selected_post['filename']} not found")

        # Remove from posts list
        posts.pop(post_number - 1)

        # Save updated posts.json
        save_posts(posts)
        print(f"✓ Updated posts.json")

        print(f"\n✓ Successfully deleted post: {selected_post['title']}")

    except ValueError:
        print("Error: Please enter a valid number")
    except KeyboardInterrupt:
        print("\n\nCancelled.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
