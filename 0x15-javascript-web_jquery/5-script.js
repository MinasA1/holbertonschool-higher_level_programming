$('#add_item').click(function () {
  $('<li>Item</li>').insertAfter('ul.my_list>li:last');
});
