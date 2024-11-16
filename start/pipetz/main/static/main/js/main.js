
// Код для работы с модальным окном
document.addEventListener("DOMContentLoaded", function () {
    // Открытие модального окна
    document.getElementById("btn-open").addEventListener("click", function () {
        document.getElementById("competition-modal").style.display = "flex";
    });

    // Закрытие модального окна
    document.getElementById("close-modal").addEventListener("click", function () {
        closeModal();
    });

    // Закрытие модального окна при нажатии на клавишу "Esc"
    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closeModal();
        }
    });

    // Закрытие модального окна при клике вне его
    document.addEventListener("click", function (event) {
        var modal = document.getElementById("competition-modal");
        if (event.target === modal) {
            closeModal();
        }
    });

    function closeModal() {
        document.getElementById("competition-modal").style.display = "none";
        resetForm();
    }

    // Сброс формы
    function resetForm() {
        var container = document.getElementById("students-container");
        container.innerHTML = `
            <div class="form-group student-entry">
                <input type="text" name="student-name" placeholder="ФИО студента">
                <input type="email" name="student-email" placeholder="Эл. почта">
                <span class="remove-student">&times;</span>
            </div>
        `;

        // Переназначить слушатель для удаления студента
        document.querySelectorAll(".remove-student").forEach(function (removeButton) {
            removeButton.addEventListener("click", function () {
                container.removeChild(this.parentElement);
            });
        });
    }

    // Функция для получения CSRF токена из куки
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Добавление нового студента
    document.getElementById('add-student').addEventListener('click', function() {
        let container = document.getElementById('students-container');
        let studentEntry = document.createElement('div');
        studentEntry.className = 'form-group student-entry';
        studentEntry.innerHTML = `
            <input type="text" name="student-name" placeholder="ФИО студента">
            <input type="email" name="student-email" placeholder="Эл. почта">
            <span class="remove-student">&times;</span>
        `;
        container.appendChild(studentEntry);

        // Добавление обработчика события для удаления студента
        studentEntry.querySelector('.remove-student').addEventListener('click', function() {
            container.removeChild(studentEntry);
        });
    });

    // Добавление обработчика события на кнопку "Участвовать"
    document.getElementById('participate-button').addEventListener('click', function() {
        // Собираем данные из формы
        let competitionId = document.getElementById('competition').value;
        let students = [];

        document.querySelectorAll('.student-entry').forEach(function(entry) {
            let studentName = entry.querySelector('input[name="student-name"]').value;
            let studentEmail = entry.querySelector('input[name="student-email"]').value;

            if (studentName && studentEmail) {
                students.push({ name: studentName, email: studentEmail });
            }
        });

        if (competitionId && students.length > 0) {
            // Формируем JSON объект для отправки на сервер
            let participantData = {
                competition_id: competitionId,
                students: students
            };

            // Отправляем данные на сервер
            fetch('/register_participant/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(participantData)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('пользователь зарегистрирован');
                console.log(data);
                closeModal(); // Закрываем модальное окно после успешной регистрации
            })
            .catch(error => {
                console.error('Error:', error);
            });
        } else {
            console.error('One or more input fields are null or empty.');
        }
    });

    // Изначально вызовем resetForm для установки слушателей на элементы формы
    resetForm();
});