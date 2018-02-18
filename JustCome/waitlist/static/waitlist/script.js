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
              alert("Data sent");
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

  // window.onclick = function(event) {
  //   if (!event.target.matches('.patient_button')) {
  //     var dropdowns = document.getElementByClassName("dropdown-content");
  //     var i;
  //     for (i = 0; i < dropdowns.length; i++) {
  //       var openDropDown = dropdowns[i];
  //       if (openDropdown.classList.contains('show')) {
  //         openDropdown.classList.remove('show');
  //       }
  //     }
  //   }
  // }
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
    }
  });
}

function movePrioritys(patientID){
  $.ajax({
    url: "/JustCome/waitlist/dequeue",
    data:{
      patientID : patientID,
    },
    type: "GET",
    success: function(data) {
      location.reload(true);
    },
    failure: function(xhr) {
      alert(xhr);
    }
  });
}

