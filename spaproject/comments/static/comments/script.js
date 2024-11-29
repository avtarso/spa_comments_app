document.addEventListener('DOMContentLoaded', () => {
    const commentsList = document.getElementById('comments');
    const commentForm = document.getElementById('commentForm');

    const commentUser_name = document.getElementById('commentUser_name');
    const commentE_mail = document.getElementById('commentE_mail');
    const commentHome_page = document.getElementById('commentHome_page');
    const commentText = document.getElementById('commentText');

    // Получение комментариев
    const fetchComments = async () => {
        try {
            const response = await fetch('/api/comments/');
            if (!response.ok) throw new Error('Ошибка при получении комментариев');
            const comments = await response.json();
            commentsList.innerHTML = '';
            comments.forEach(comment => {
                const li = document.createElement('li');
                li.textContent = `${comment.user_name} - ${comment.text}`;
                commentsList.appendChild(li);
            });
        } catch (error) {
            console.error(error);
            commentsList.innerHTML = '<li>Не удалось загрузить комментарии</li>';
        }
    };

    // Добавление комментария
    commentForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Проверка обязательных полей
        if (!commentUser_name.value || !commentE_mail.value || !commentText.value) {
            alert('Пожалуйста, заполните обязательные поля!');
            return;
        }

        const response = await fetch('/api/comments/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_name: commentUser_name.value,
                e_mail: commentE_mail.value,
                home_page: commentHome_page.value || null, // Пустое значение передаём как null
                text: commentText.value,
            }),
        });

        if (response.ok) {
            commentUser_name.value = '';
            commentE_mail.value = '';
            commentHome_page.value = '';
            commentText.value = '';
            fetchComments();
        } else {
            alert('Ошибка при добавлении комментария');
        }
    });

    fetchComments();
});
