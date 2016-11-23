$(function () {

    $(".js-create-book").click(function (){
        $.ajax({
            url: '/livros/criar',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-book").modal("show");
            },
            success: function (data) {
                $("#modal-book .modal-content").html(data.html_form);
            }
        })
    })

});
