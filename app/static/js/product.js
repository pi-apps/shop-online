$(document).ready(function() {
  $('.product-list li').click(function() {
    var productId = $(this).data('product-id');
    $.ajax({
      type: 'GET',
      url: '/product/' + productId,
      success: function(data) {
        $('#product-detail').html(data);
      }
    });
  });
});
