$(document).ready(function () {
    $('.title').fadeIn(1500);
    $('.titulo').fadeIn(1000);
    $('.cvs').fadeIn(3000);
      $('#L11').hide();
      $('#L22').hide();
      $('#L33').hide();
      $('#L44').hide();

      $("#L1").click(function () {
          $('#1').slideToggle();
          $(this).hide();
          $('#L11').show();
      });
      $("#L11").click(function () {
          $('#1').slideToggle();
          $(this).hide();
          $('#L1').show();
      });
      
      $("#L2").click(function () {
          $('#2').slideToggle();
          $(this).hide();
          $('#L22').show();
      }); 
      $("#L22").click(function () {
          $('#2').slideToggle();
          $(this).hide();
          $('#L2').show();
      });

      $("#L3").click(function () {
          $('#3').slideToggle();
          $(this).hide();
          $('#L33').show();
      });
      $("#L33").click(function () {
          $('#3').slideToggle();
          $(this).hide();
          $('#L3').show();
      });

      $("#L4").click(function () {
          $('#4').slideToggle();
          $(this).hide();
          $('#L44').show();
      });
      $("#L44").click(function () {
          $('#4').slideToggle();
          $(this).hide();
          $('#L4').show();
      });
  });