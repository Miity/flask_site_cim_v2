function pageUpdateAjax(data){
    $.ajax({
        type: "POST",
        url: '/admin/page_update_ajax',
        data: JSON.stringify(data),
        dataType:'json',
        contentType: "application/json; charset=utf-8",
        async: false,
        });
}