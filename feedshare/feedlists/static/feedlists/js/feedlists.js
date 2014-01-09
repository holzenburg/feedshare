jQuery(function($) {
    $('.help-block').prepend('<i class="fa fa-info-circle"></i> ');

    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    	$('body').addClass('mobile');
    } else {
    	$('body').addClass('desktop');
    }
});


// Bootstrap tagsinput with custom typeahead support using
// https://github.com/timschlechter/bootstrap-tagsinput
// http://twitter.github.io/typeahead.js

(function($){
    $.fn.extend({ 
        autocomplete: function(url) {
            return this.each(function() {
        		$(this).typeahead({
        			remote: url,
        		}).bind('typeahead:selected', $.proxy(function (obj, result) {
        			$(this).val(result.value);
        		}, $(this)));
            });
        },
        autocompleteTags: function(url) {
            return this.each(function() {
        		$(this).tagsinput('input').typeahead({
        			remote: url,
        		}).bind('typeahead:selected', $.proxy(function (obj, result) {
        			this.tagsinput('add', result.value);
        			this.tagsinput('input').typeahead('setQuery', '');
        		}, $(this)));
            });
        }
    });
})(jQuery);