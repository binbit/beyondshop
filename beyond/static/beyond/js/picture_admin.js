/**
 * Created by BIN on 22.07.2015.
 */
(function($) {
    $(document).ready(function() {
        $('td.field-Main > input').click(function(){
            $('td.field-Main > input:not(#'+ $(this).attr('id') +')').each(function(){
                $(this).attr('checked', false);
            });
        });
    });
})(django.jQuery);