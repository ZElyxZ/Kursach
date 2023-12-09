$(document).ready(function() {
    $("#productsaveform").submit(function(event) {
        event.preventDefault(); // Отменяет стандартное поведение отправки формы
        var instockValue = $("#checkbox-08ac").is(":checked") ? 'true' : 'false';
        var formData = $(this).serialize();
        formData += "&instock=" + instockValue;


        $.ajax({
            type: "POST",
            url: "/save_product/",
            data: formData,
            success: function(response) {
                if (response.success) {
                    alert("Запись успешно сохранена!");
                    // Можете добавить код для перенаправления на другую страницу или выполнения других действий
                } else {
                    alert("Произошла ошибка при сохранении записи.");
                }
            },
            error: function(xhr, status, error) {
                alert("Произошла ошибка при выполнении запроса: " + error);
            }
        });
    });
});