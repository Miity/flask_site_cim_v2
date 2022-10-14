const add_block = (type, page_id) => {
    data = {'type': type, 'page_id': page_id}
    $.ajax({
        type: "POST",
        url: '/block/block_add',
        data: JSON.stringify({'data':data}),
        dataType:'json',
        contentType: "application/json; charset=utf-8",
        async: false,

        error: function(error){
              console.log("Error:");
              console.log(error);
        },
        });

        reload_page_info()
}

function block_remove(obj, data){
    $.ajax({
        type: "POST",
        url: '/block/block_update',
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType:'json',
        });
    obj.parentElement.parentElement.remove()

    sort_data()
    }

function update(data){
    $.ajax({
        type: "POST",
        url: '/block/block_update',
        data: JSON.stringify(data),
        dataType:'json',
        contentType: "application/json; charset=utf-8",
        async: false,
        });
}

function uploadFiles(inp_id, data) {
    let files = document.getElementById(inp_id).files;
    let formData = new FormData(); 
    
    for (let i = 0; i< files.length ; i++){
        formData.append("file"+i, files[i]);
    }
    formData.append('data', JSON.stringify(data));

    $.ajax({
        type: "POST",
        url: '/block/uploadFiles',
        data: formData,
        processData: false,
        contentType: false,
        });
}