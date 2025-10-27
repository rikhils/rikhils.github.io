// Get the post filename from URL parameter
const urlParams = new URLSearchParams(window.location.search);
const postFilename = urlParams.get('post');

if (!postFilename) {
    document.getElementById('post-content').innerHTML = '<p>No post specified.</p>';
} else {
    // Load and render the markdown post
    fetch(`posts/${postFilename}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Post not found');
            }
            return response.text();
        })
        .then(markdown => {
            const html = marked.parse(markdown);
            document.getElementById('post-content').innerHTML = html;

            // Update page title with first h1 found
            const titleMatch = markdown.match(/^#\s+(.+)$/m);
            if (titleMatch) {
                document.title = titleMatch[1];
            }
        })
        .catch(error => {
            console.error('Error loading post:', error);
            document.getElementById('post-content').innerHTML = '<p>Error loading post.</p>';
        });
}
