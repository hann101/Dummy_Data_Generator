$("form[name=signup_form").submit(function(e) {
  // singup form 버튼이 눌리면 발생하는 이벤트
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/user/signup",
      //  signd 으로 요청 들어오면 전송.
      type: "POST",
      data: data,
      dataType: "json",
      success: function(resp) {
        // window.location.href = "/dashboard/";
        console.log(resp);
      },
      error: function(resp) {
        // $error.text(resp.responseJSON.error).removeClass("error--hidden");
        console.log(resp);
      }
    });
  
    e.preventDefault();
  });
  
  // $("form[name=login_form").submit(function(e) {
  
  //   var $form = $(this);
  //   var $error = $form.find(".error");
  //   var data = $form.serialize();
  
  //   $.ajax({
  //     url: "/user/login",
  //     type: "POST",
  //     data: data,
  //     dataType: "json",
  //     success: function(resp) {
  //       window.location.href = "/dashboard/";
  //     },
  //     error: function(resp) {
  //       $error.text(resp.responseJSON.error).removeClass("error--hidden");
  //     }
  //   });
  
  //   e.preventDefault();
  // });