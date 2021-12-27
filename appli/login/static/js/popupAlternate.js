var $signUp = $('.signUp');
var $signIn = $('.signIn');


    $(".btn-member").click(function() {
      $signUp.fadeOut('slow');
      $signIn.fadeIn('slow');
      $('.signInSect').toggleClass('hide');
      $('.signUpSect').removeClass('hide');
    });
   $(".btn-back").click(function() {
      $signIn.fadeOut('slow');
      $signUp.fadeIn('slow');
      $('.signUpSect').toggleClass('hide');
      $('.signInSect').removeClass('hide');
    });

  