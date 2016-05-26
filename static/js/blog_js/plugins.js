// Avoid `console` errors in browsers that lack a console.
(function() {
    var method;
    var noop = function () {};
    var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'
    ];
    var length = methods.length;
    var console = (window.console = window.console || {});

    while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
            console[method] = noop;
        }
    }
}());
tinyMCE.init({
        theme : "advanced",
        mode : "textareas",
        plugins : "preview",
        theme_advanced_buttons3_add : "preview",
        plugin_preview_width : "1500",
        plugin_preview_height : "1600"
});
tinymce.init({
  selector: "textarea",  // change this value according to your HTML
  toolbar: "image",
  plugins: "image imagetools"
});
tinymce.init({
  selector: "textarea",  // change this value according to your HTML
  plugins: "insertdatetime",
  menubar: "insert",
  toolbar: "insertdatetime"
});

// Place any jQuery/helper plugins in here.
