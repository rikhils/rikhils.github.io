# Simple Blog

A minimalist blog with an early internet aesthetic. Just HTML, CSS, and markdown files.

## Structure

```
.
├── index.html          # Landing page
├── blog.html           # Blog posts listing
├── post.html           # Individual post viewer
├── style.css           # Minimal styling
├── blog.js             # Script to list posts
├── post.js             # Script to render markdown
├── posts.json          # List of all posts
└── posts/              # Directory containing markdown posts
    ├── 2024-01-15-welcome.md
    └── 2024-01-20-second-post.md
```

## Adding a New Post

1. Create a new markdown file in the `posts/` directory
2. Name it with the format: `YYYY-MM-DD-title.md`
3. Write your content in markdown
4. Update `posts.json` to include your new post:
   ```json
   {
     "filename": "YYYY-MM-DD-title.md",
     "title": "Your Post Title",
     "date": "Month DD, YYYY"
   }
   ```
5. Add it to the top of the array (newest posts first)

## Deploying to GitHub Pages

1. Create a new repository on GitHub (e.g., `username.github.io`)
2. Initialize git and push this code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/username/username.github.io.git
   git push -u origin main
   ```
3. Go to your repository settings > Pages
4. Set source to "Deploy from a branch"
5. Select the `main` branch and `/` (root) folder
6. Save and wait a few minutes
7. Your site will be available at `https://username.github.io`

## Local Development

To view locally, you need to serve the files with a local web server (due to CORS restrictions with `fetch()`):

```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js (if you have npx)
npx serve
```

Then open `http://localhost:8000` in your browser.
