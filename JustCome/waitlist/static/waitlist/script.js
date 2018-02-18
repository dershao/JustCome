$(document).ready(function() {
  //THis is te code for enqueuing
  $("#submit").click(function() {
    var id = $("#phone").val();
    var priority = $("#priority").val();
    $.ajax({
            url:"/JustCome/waitlist/enqueue",
            type: "get",
            data: {
              patientID: id,
              priority: priority,
            },
            dataType: "json",
            success: function(response) {

            },
            failure: function(xhr) {
              alert("failed");
            },
          });
    location.reload();
  });
//This is the code for dequeuing
  $("#next").click(function() {
    $.ajax({
            url:"/JustCome/waitlist/dequeue",
            type: "get",
            success: function(data) {

            },
            failure: function(xhr) {
              alert("failed");
            },
          });
  });
  location.reload();
});
