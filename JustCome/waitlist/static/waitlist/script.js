$(document).ready(function() {
  //THis is te code for enqueuing 
  $("#enque").click(function() {
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
//This is the code for dequeuing 
  $("#dequeue").click(function() {
    $.ajax({
            url:"/JustCome/waitlist/dequeue",
            type: "GET",
            success: function(response) {
              alert("Data sent");
            },
            failure: function(xhr) {
              alert("failed");
            },
          });
  });
});



