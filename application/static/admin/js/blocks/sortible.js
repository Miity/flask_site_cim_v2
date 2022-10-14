var sortible = () => $("#blocks").sortable({
  items: ".block",
  update: function( event, ui ) {
    sort_data()      
  }
});
sortible()

function sort_data(){
  let order_items = document.getElementById('blocks').children
  let ids = []
  for (let i = 0 ; i < order_items.length ; i++ ){
    console.log(order_items[i])
    ids.push(order_items[i].id)
  }
  $.ajax({
          type: "POST",
          url: '/block/block_update',
          data: JSON.stringify({'type':'reorder', 'block_ids':ids}),
          dataType:'json',
          contentType: "application/json; charset=utf-8",
          async: false,
      })
}