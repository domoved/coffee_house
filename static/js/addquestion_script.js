function addQuestion() {
    var formset = $('#questions').data('prefix');
    var questionIndex = parseInt($('#id_' + formset + '-TOTAL_FORMS').val());
    var newQuestion = $('#empty_form').html().replace(/__prefix__/g, questionIndex);
    $('#questions').append(newQuestion);
    $('#id_' + formset + '-TOTAL_FORMS').val(questionIndex + 1);
}

function addAnswer(prefix) {
    var formCount = $('#id_' + prefix + '-answer_set-TOTAL_FORMS').val();
    var newAnswer = $('#empty_answer_form').html().replace(/__prefix__/g, formCount);
    $('#answers-' + prefix).append(newAnswer);
    $('#id_' + prefix + '-answer_set-TOTAL_FORMS').val(parseInt(formCount) + 1);
}