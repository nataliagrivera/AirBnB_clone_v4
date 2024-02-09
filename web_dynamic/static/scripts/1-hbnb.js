#!/usr/bin/node
$(document).ready(function () {
  const amenityIds = {};

  $('input[type=checkbox]').click(function () {
    const myListName = [];
    const myId = [];
    $('input[type="checkbox"]:checked').each(function () {
      myListName.push($(this).attr('data-name'));
      myId.push($(this).attr('data-id'));
    });
    if (myListName.lenght === 0) {
      $('.amenities h4').html('&nbsp;');
    } else {
      $('.amenities h4').text(myListName.join(', '));
    }
    console.log(myId);
  });
});
