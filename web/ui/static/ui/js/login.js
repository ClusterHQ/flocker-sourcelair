$('form.login-form').on('submit', function() {
    var form = $(this);
    var url = '/api/auth/login/';
    var data = {};
    var errCondition = false;

    //Loop through and grab only the value of the attribute id.
    form.find('[id]').each(function() {
        var element = $(this);
        var idValue = element.attr('id');
        var value = element.val();

        data[idValue] = value;
    });

    $.ajax({
        url   : url,
        type  : 'POST',
        data  : data,
    }).done(function(data, textStatus, req) {
        // Place code here to redirect to /terminal
        window.location.href = '/terminal';
    }).fail(function(req, textStatus, errorThrown) {
        // Place code here to show error from req.responseJSON object
        // Form key: error
        $('div.alert').remove(); //In case of previous warning, remove the warning(div) so that the new one appears.
        var JSONresponse = req.responseJSON;
        console.log(textStatus);
        console.log(errorThrown);
        var errorThrownMsg = '<div class="alert alert-warning alert-block space fade in"><a href="#" class="close" data-dismiss="alert">&times;</a><strong>' + errorThrown + ' : ' + ' </strong> Enter username or password right. </div>';

        for( var key in JSONresponse){
            var warning = '<div class="alert alert-warning alert-block space fade in"><a href="#" class="close" data-dismiss="alert">&times;</a><strong>Form ' + key + ' error :</strong> ' + JSONresponse[key] + '</div>';
            $('.error-warnings').append(warning);
        }
        $('.error-warnings').append(errorThrownMsg);
    });
    return false; //Prevent default.
});