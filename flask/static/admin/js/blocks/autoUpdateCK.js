function autoUpdateCK(){
    let editors = CKEDITOR.instances
    for (i in editors){
      console.log(i)
      let ck = CKEDITOR.instances[i]
      ck.on('change', function() { 
          let data = {'type': 'text','id':ck.name, 'value':ck.getData()}
          $.ajax({
              type: "POST",
              url: '/block/block_update',
              data: JSON.stringify(data),
              contentType: "application/json; charset=utf-8",
              dataType:'json',
              });
      });
    }
  }