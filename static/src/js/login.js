(function($, window, document) {
  $(function() {
    $("#signup").click(showSignupOptions);
  });

  function showSignupOptions(event) {
    event.preventDefault();
    $(".ui.page.dimmer").dimmer("show");
  }
})(window.jQuery, window, document);
