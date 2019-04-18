(function($, window, document) {
  $(function() {
    $("#scholarship").DataTable();

    $("#filterButton").click(toggleFilter);

    $(".message .close").on("click", closeMessage);
  });

  function toggleFilter() {
    $("#filterContent").transition({
      animation: "slide down",
      duration: "0.7s"
    });
  }

  function closeMessage() {
    $(this)
      .closest(".message")
      .transition("fade");
  }
})(window.jQuery, window, document);
