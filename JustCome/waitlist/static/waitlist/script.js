$(document).ready(function() {
  //This is te code for enqueuing
  $("#submit").click(function() {
    var id = $("#id").val();
    var number = $("#phoneNumber").val();
    var priority = $("#priority-select").val();
    if(!id || !number || !priority){
      alert("Form Incomplete.");
      return;
    }
    $.ajax({
            url:"/JustCome/waitlist/enqueue",
            type: "GET",
            data: {
              patientID: id,
              phoneNumber: number,
              priority: priority,
            },
            success: function(response) {
              location.reload(true);
            },
            failure: function(xhr) {
              alert("failed");
            },
          });
  });

  $(".patient_button").click(function() {
    var dropdown = $(this).siblings('.dropdown-content');
    dropdown.toggle();
  });

  window.onclick = function(event) {
    if (!event.target.matches('.patient_button')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        dropdowns[i].style.display = 'none';
      }
    }
  }
});

//Function to dequue a patient
function dequeue(phoneNumber){
  $.ajax({
    url: "/JustCome/waitlist/dequeue",
    data:{
      phoneNumber : phoneNumber,
    },
    type: "GET",
    success: function(data) {
      location.reload(true);
    },
    failure: function(xhr) {
      alert(xhr);
    },
  });
}

function movePriorities(patientID, priority){
  $.ajax({
    url: "/JustCome/waitlist/move",
    data:{
      patientID : patientID,
      priority : priority
    },
    type: "GET",
    success: function(data) {
      location.reload(true);
    },
    failure: function(xhr) {
      alert(xhr);
    },
  });
}
