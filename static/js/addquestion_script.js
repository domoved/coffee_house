document.addEventListener('DOMContentLoaded', function() {
    var questionSection = document.getElementById('question-section');
    var questionCount = 0;

    questionSection.addEventListener('click', function(event) {
        var target = event.target;
        if (target.classList.contains('add-question-btn')) {
            addQuestionField();
        } else if (target.classList.contains('add-answer-btn')) {
            addAnswerField(target);
        }
    });

    function addQuestionField() {
        var questionForm = document.createElement('div');
        questionForm.classList.add('question-form');
        questionForm.dataset.questionIndex = questionCount;
        questionForm.innerHTML = `
            <label for="id_question_text_${questionCount}">Текст вопроса:</label>
            <input type="text" name="question_text_${questionCount}" id="id_question_text_${questionCount}">
            <button type="button" class="btn btn-primary add-answer-btn">Добавить ответ</button>
            <div class="answers mt-2"></div>
            <br>
        `;
        questionSection.appendChild(questionForm);
        questionCount++;
    }

    function addAnswerField(button) {
        var questionIndex = button.parentNode.dataset.questionIndex;
        var answerIndex = button.parentNode.querySelectorAll('.answer-form').length;
        var answerForm = document.createElement('div');
        answerForm.classList.add('answer-form');
        answerForm.innerHTML = `
            <label for="id_answer_text_${questionIndex}_${answerIndex}">Текст ответа:</label>
            <input type="text" name="answer_text_${questionIndex}_${answerIndex}" 
            id="id_answer_text_${questionIndex}_${answerIndex}">
            <label for="id_is_correct_${questionIndex}_${answerIndex}">Правильный ответ:</label>
            <input type="checkbox" name="is_correct_${questionIndex}_${answerIndex}" 
            id="id_is_correct_${questionIndex}_${answerIndex}">
        `;
        button.parentNode.querySelector('.answers').appendChild(answerForm);
    }
});
