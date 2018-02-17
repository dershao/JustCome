$(document).ready(function() {
  $("#enque").click(function()
    $.ajax({
            url:"/JustCome/waitlist/data",
            type: "get",
            data: {
              delta: 1,
            },
            success: function(response) {
              alert("Data sent");
            },
            failure: function(xhr) {
              alert("failed");
            },
          });
  });
});
