$(function() {
    $("div.inline-group").sortable({
        placeholder: 'ui-state-highlight',
        forcePlaceholderSize: 'true',
        items: 'div.inline-related',
        update: function() {
            $(this).find('div.inline-related').each(function(i) {
                if ($(this).find('.vTextField').val()) {
                    $(this).find('input[id$=ordering]').val(i+1);
                }
        });
        }
    });
    $("div.inline-group").disableSelection();
	$('div.inline-related h3').css('cursor', 'move');
});

$(document).ready(function(){
    $(this).find('input[id$=ordering]').parent('div').parent('div').hide()
});
