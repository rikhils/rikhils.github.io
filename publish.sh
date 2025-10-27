#!/bin/bash
# Publish blog updates to GitHub
# Uses the latest post title as the commit message

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Publishing blog updates...${NC}"

# Check if we're in a git repo
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not a git repository. Run 'git init' first."
    exit 1
fi

# Get the latest post title from posts.json
if [ ! -f "posts.json" ]; then
    echo "Error: posts.json not found"
    exit 1
fi

# Extract the first post title using Python (more reliable than jq)
LATEST_TITLE=$(python3 -c "
import json
with open('posts.json', 'r') as f:
    posts = json.load(f)
    if posts:
        print(posts[0]['title'])
    else:
        print('Update blog')
" 2>/dev/null)

# Fallback if extraction fails
if [ -z "$LATEST_TITLE" ]; then
    LATEST_TITLE="Update blog"
fi

COMMIT_MESSAGE="New post: $LATEST_TITLE"

echo -e "${GREEN}✓${NC} Using commit message: $COMMIT_MESSAGE"

# Git add all changes
echo -e "${BLUE}Adding changes...${NC}"
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Commit with the latest post title
echo -e "${BLUE}Committing changes...${NC}"
git commit -m "$COMMIT_MESSAGE"

# Push to remote
echo -e "${BLUE}Pushing to remote...${NC}"
git push

echo -e "${GREEN}✓ Blog published successfully!${NC}"
