let load_page = (element_id, url) => {
    const element = document.getElementById(element_id)
    $.ajax({
      type: "GET",
      url: url,
      async: false,
      success: function(data){
        element.innerHTML = data['template']
        CKEDITOR.replaceAll()
        autoUpdateCK()
        sortible()
      },
      error: function(error){
            console.log("Error:");
            console.log(error);
    },
    });
}