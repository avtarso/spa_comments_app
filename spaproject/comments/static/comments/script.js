document.addEventListener('DOMContentLoaded', () => {

    const commentsList = document.getElementById('comments');
    const commentForm = document.getElementById('commentForm');

    const commentUser_name = document.getElementById('commentUser_name');
    const commentE_mail = document.getElementById('commentE_mail');
    const commentHome_page = document.getElementById('commentHome_page');
    const commentText = document.getElementById('commentText');

    const captchaImage = document.getElementById('captchaImage');
    const refreshCaptcha = document.getElementById('refreshCaptcha');
    const captchaAnswer = document.getElementById('captchaAnswer');
    const captchaKey = document.getElementById('captchaKey');

    const loadCaptcha = async () => {
        const response = await fetch('/api/get-captcha/');
        if (response.ok) {
            const data = await response.json();
            captchaImage.src = data.captcha_url;
            captchaKey.value = data.captcha_key;
        } else {
            alert('Ошибка при загрузке капчи');
        }
    };

    refreshCaptcha.addEventListener('click', loadCaptcha);

    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    const getHeadersWithCSRF = () => ({
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
    });

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
        if (!commentUser_name.value || !commentE_mail.value || !commentText.value || !captchaAnswer.value) {
            alert('Пожалуйста, заполните обязательные поля!');
            return;
        }

        // Проверка капчи
        const captchaResponse = await fetch('/api/check-captcha/', {
            method: 'POST',
            headers: getHeadersWithCSRF(),
            body: JSON.stringify({
                captcha_key: captchaKey.value,
                captcha_answer: captchaAnswer.value,
            }),
        });

        const captchaResult = await captchaResponse.json();
        if (!captchaResult.success) {
            alert('Неверная капча!!!');
            loadCaptcha();
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
                home_page: commentHome_page.value || null,
                text: commentText.value,
            }),
        });

        if (response.ok) {
            commentUser_name.value = '';
            commentE_mail.value = '';
            commentHome_page.value = '';
            commentText.value = '';
            captchaAnswer.value = '';
            fetchComments();  
            loadCaptcha();
        } else {
            alert('Ошибка при добавлении комментария');
        }
    });

    fetchComments();
    loadCaptcha();
});
