$(document).ready(function() {
  //THis is te code for enqueuing
  $("#submit").click(function() {
    var id = $("#phone").val();
    var priority = $("#priority").val();
    $.ajax({
            url:"/JustCome/waitlist/enqueue",
            type: "GET",
            data: {
              patientID: id,
              priority: priority,
            },
            dataType: "json",
            success: function(response) {
              location.reload(true);
            },
            failure: function(xhr) {
              alert("failed");
            },
          });
  });
//This is the code for dequeuing
  $("#next").click(function() {
    $.ajax({
            url: "/JustCome/waitlist/dequeue",
            type: "GET",
            success: function(data) {
              location.reload(true);
            },
            failure: function(xhr) {
              alert(xhr);
            },
          });
  });

  $(".low_patient").click(function() {
    $.ajax({
            url: "/JustCome/waitlist/dequeue",
            type: "GET",
            success: function(data) {
              alert(data);
            },
            failure: function(xhr) {
              alert(xhr);
            },
          });
    });
});
