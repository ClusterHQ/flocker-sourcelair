$('form.registration-form').on('submit', function() {
  console.log('Checked');
  var form = $(this);
  var url = '/api/auth/register/';
  var data = {};

  //Loop through and grab only the value of 'id ' attr
  form.find('[id]').each(function() {
    var element = $(this); //this is a reference or the object that contains the elements that ref.find found
    var idValue = element.attr('id');
    var value = element.val();

    data[idValue] = value;
  });
  console.log(data);

  $.ajax({
    url   : url,
    type  : 'POST',
    data  : data,
  }).done(function(data, textStatus, req) {
      // Place code here to redirect to /terminal
  }).fail(function(req, textStatus, errorThrown) {
      // Place code here to show error from req.responseJSON object
      // Form key: error
  });

  return false;
});
