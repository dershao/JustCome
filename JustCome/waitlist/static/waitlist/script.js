$(document).ready(function() {
<<<<<<< HEAD
  var id = "6131231234"
  var priority = "high"
=======
  //THis is te code for enqueuing 
>>>>>>> 50f3cd2c187913c0b9c3fccc7523adf5550619e1
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
//This is the code for dequeuing 
  $("#dequeue").click(function() {
    $.ajax({
            url:"/JustCome/waitlist/dequeue",
            type: "GET",
            success: function(data) {
              alert(data);
            },
            failure: function(xhr) {
              alert("failed");
            },
          });
  });
});



