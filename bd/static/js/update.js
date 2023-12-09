$(document).ready(function() {
        $("#select-bec0").change(function() {
            updateProductFields();
        });
    });
function updateProductFields() {
         var productId = parseInt($("#select-bec0").val(), 10);
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8010/get_product_data/",
            data: {'product_id': productId},
            success: function(data) {
                console.log(data);
                $("#name-e2a4").val(data.productname);
                $("#message-e2a4").val(data.aboutproduct);
                $("#text-419e").val(data.price);
                $("#checkbox-08ac").prop('checked', data.instock === 'true');




            var quantitySelect = $("#select-9eef");
            quantitySelect.empty();

            // Проходимся по всем значениям и добавляем их в список
            for (var i = 0; i < data.all_quantities.length; i++) {
                var option = $("<option>", {value: data.quantityid[i], text: data.all_quantities[i]});
                quantitySelect.append(option);
            }
            var companySelect = $("#select-7ff4");
            companySelect.empty();

            // Проходимся по всем значениям и добавляем их в список
            for (var j = 0; j < data.all_companies.length; j++) {
                var option = $("<option>", {value: data.companyid[j], text: data.all_companies[j]});
                companySelect.append(option);
            }

            },
            error: function(xhr, status, error) {
            // В случае ошибки выведите ее в консоль
            console.error(error);
            }
        });
    }