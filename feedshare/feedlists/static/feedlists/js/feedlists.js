jQuery(function($) {
    $('.help-block').prepend('<i class="fa fa-info-circle"></i> ');
});


(function($){
    $.fn.extend({ 
        autocompleteTags: function(url) {
            return this.each(function() {
        		$(this).tagsinput();
 
        		// Adding custom typeahead support using
        		// http://twitter.github.io/typeahead.js
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