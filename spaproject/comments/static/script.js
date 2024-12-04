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
    const captchaKeyInput = document.getElementById('captchaKey');

    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    const socket = new WebSocket(
        window.location.protocol === 'https:' 
            ? (window.location.hostname === 'spa.up.railway.app'
                ? 'wss://spa.up.railway.app/ws/comments/'
                : 'wss://harmonious-rebirth-production.up.railway.app/ws/comments/'
            )
            : 'ws://127.0.0.1:8000/ws/comments/'
    );

    const quill = new Quill('#commentTextEditor', {
        theme: 'snow',
        placeholder: 'Write your comment...',
        modules: {
            toolbar: [
                ['link', 'code', 'italic', 'bold']
            ]
        }
    });

    const getHeadersWithCSRF = () => ({
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
    });

    const loadCaptcha = async () => {
        try {
            const response = await fetch('/api/get-captcha/');
            if (!response.ok) throw new Error('Ошибка при загрузке капчи 1');
            const captchaKey = response.headers.get('Captcha-Key');
            const blob = await response.blob();
            const captchaUrl = URL.createObjectURL(blob);
            captchaImage.src = captchaUrl;
            captchaKeyInput.value = captchaKey;
         } catch (error) {
            alert('Ошибка при загрузке капчи 2');
        }
    };

    const fetchComments = async () => {
        try {
            const response = await fetch('/api/comments/');
            if (!response.ok) throw new Error('Ошибка при получении комментариев');
            const comments = await response.json();
            commentsList.innerHTML = '';
            comments.forEach(comment => {
                const li = document.createElement('li');
                // li.textContent = `${comment.user_name} - ${comment.text}`;
                li.innerHTML = `${comment.user_name} - ${comment.text}`;
                commentsList.appendChild(li);
            });
        } catch (error) {
            commentsList.innerHTML = '<li>Не удалось загрузить комментарии</li>';
        }
    };

    socket.onopen = () => {
        console.log("WebSocket соединение установлено");
    };

    socket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        const comment = data.message;
        const li = document.createElement('li');
        li.innerHTML = `${comment.user_name} - ${comment.text}`;
        document.getElementById('comments').appendChild(li);
    };


    commentForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const usernameRegex = /^[a-zA-Z0-9]+$/;
        if (!usernameRegex.test(commentUser_name.value)) {
            alert('Имя пользователя может содержать только латинские буквы и цифры!');
            return;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(commentE_mail.value)) {
            alert('Введите корректный адрес электронной почты!');
            return;
        }

        if (quill.root.innerHTML != '<p><br></p>') {
            commentText.value = quill.root.innerHTML; 
        }        

        if (!commentUser_name.value || !commentE_mail.value || !commentText.value || !captchaAnswer.value) {
            alert('Пожалуйста, заполните обязательные поля!');
            return;
        }

        try {
            const captchaResponse = await fetch('/api/verify-captcha/', {
                method: 'POST',
                headers: getHeadersWithCSRF(),
                body: JSON.stringify({
                    captcha_key: captchaKey.value,
                    captcha_value: captchaAnswer.value,
                }),
            });

            const captchaResult = await captchaResponse.json();
            if (!captchaResult.success) {
                alert('Неверная капча!');
                loadCaptcha();
                return;
            }

            const response = await fetch('/api/comments/', {
                method: 'POST',
                headers: getHeadersWithCSRF(),
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
                quill.root.innerHTML = '';
                captchaAnswer.value = '';
                
                fetchComments();
                loadCaptcha();
            } else {
                // Обработка ошибок от сервера
                const errorData = await response.json();
                // console.log(errorData);
                if (errorData && typeof errorData === 'object') {
                    const errorMessages = Object.entries(errorData)
                        .map(([field, messages]) => `${messages.join(', ')}`)
                        .join('\n');
                    alert(`Ошибка при добавлении комментария:\n${errorMessages}`);
                    captchaAnswer.value = '';
                    loadCaptcha();
                } else {
                    throw new Error('Ошибка при добавлении комментария');
                }
            }
        } catch (error) {
            alert(error.message);
            captchaAnswer.value = '';
        }
    });

    refreshCaptcha.addEventListener('click', loadCaptcha);

    fetchComments();
    loadCaptcha();
});
