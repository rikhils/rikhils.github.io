// Load and display list of blog posts
fetch('posts.json')
    .then(response => response.json())
    .then(posts => {
        const postsListDiv = document.getElementById('posts-list');

        if (posts.length === 0) {
            postsListDiv.innerHTML = '<p>No posts yet.</p>';
            return;
        }

        let html = '';
        posts.forEach(post => {
            html += `
                <div class="post-item">
                    <a href="post.html?post=${post.filename}">${post.title}</a>
                    <br>
                    <span class="post-date">${post.date}</span>
                </div>
            `;
        });

        postsListDiv.innerHTML = html;
    })
    .catch(error => {
        console.error('Error loading posts:', error);
        document.getElementById('posts-list').innerHTML = '<p>Error loading posts.</p>';
    });
