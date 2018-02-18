$(document).ready(function() {
  var id = "6131231234"
  var priority = "high"
  $("#enque").click(function() {
    $.ajax({
            url:"/JustCome/waitlist/enque",
            type: "get",
            data: {
              patientID: id,
              priority: priority,
            },
            dataType: "json",
            success: function(response) {
              alert("Data sent");
            },
            failure: function(xhr) {
              alert("failed");
            },
          });
  });
});
