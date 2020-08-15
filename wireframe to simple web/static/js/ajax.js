
"use strict";

  // add an event listener to the form
  // alert(selectedId);
  // Figure out equivalents to AJAX fortune/weather examples
  // app route in server.py says /api/human/<int:human_id>

  // use id to send a get request to /api/human/<human_id>
  // Replace the function call on the line above.
  //
  // Instead of alerting the user, you need to make an AJAX request to
  // retrieve data about a human.
  //
  // Use data from the server to update the contents of #fname, #lname, and #email with their appropriate values
  // Once you retrieve the data, replace the HTML in #fname,
  // lname, and #email with the server's response
  // unlike the AJAX fortune example whiched used div tags this one
  // uses dt tags - probably data table
  // trying # like div tag with .html(response);
  // retrieve id selected

$('#get-human').on('submit', (evt) => {
  evt.preventDefault();


  const selectedId = $('#human-id').val();

    $.get(`/api/human/<int:human_id>`, (res) => {
      $('#fname').html(res.fname);
      $('#lname').html(res.lname);
      $('#email').html(res.email);
    });
  });
