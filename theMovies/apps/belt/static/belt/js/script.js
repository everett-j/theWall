// Wait for the DOM to be ready
$(function() {
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='new_trip']").validate({
      // Specify validation rules
      rules: {
        // The key name on the left side is the name attribute
        // of an input field. Validation rules are defined
        // on the right side
        destination: "required",
        startdate: "required",
        enddate: "required",
        plan: "required",
      },
      // Specify validation error messages
      messages: {
        destination: "Please enter your destination",
        startdate: "Please enter your start date",
        enddate: "Please enter your end date",
        plan: "Please enter your plan",
        
      // Make sure the form is submitted to the destination defined
      // in the "action" attribute of the form when valid
      submitHandler: function(form) {
        form.submit();
      }
    });
  });