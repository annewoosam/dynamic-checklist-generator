"use strict";

$('#get-template').on('submit', (evt) => {
  evt.preventDefault();

  const selectedId = $('#template-id').val();

  $.get(`/api/template/${selectedId}`, (res) => {
    $('#templatename').html(res.templatename);
    $('#createdby').html(res.createdby);
    $('#createdon').html(res.createdon);
  });
});
