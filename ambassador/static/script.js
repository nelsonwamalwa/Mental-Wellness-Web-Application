document.addEventListener('DOMContentLoaded', function() {
    const viewMoreButtons = document.querySelectorAll('.view-more-comments');

    viewMoreButtons.forEach(button => {
        button.addEventListener('click', function() {
            const commentWrapper = button.closest('.comment-wrapper');
            const commentsList = commentWrapper.nextElementSibling;
            if (commentsList) {
                commentsList.style.display = commentsList.style.display === 'none' ? 'block' : 'none';
                button.textContent = commentsList.style.display === 'none' ? 'View More Comments' : 'View Fewer Comments';
            }
        });
    });
});
