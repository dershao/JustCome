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
//This is the code for dequeuing
  $("#next").click(function() {
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

  $(".patient_button").click(function() {
    var dropdown = $(this).siblings('.dropdown-content');
    dropdown.toggle();
  });

  window.onclick = function(event) {
    if (!event.target.matches('.patient_button')) {
      var dropdowns = document.getElementByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropDown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
});
