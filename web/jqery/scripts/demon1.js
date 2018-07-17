$(document).ready(function(){
    main();
});


function main() {
    hidetext();
    test();
    textalert();
    $("#selecttest").append("<option value='1'>1</option>")
    $("#selecttest").append("<option>2</option>")
    $("#selecttest").append("<option>3</option>")
    $("#selecttest").append("<option>4</option>")
    $("#selecttest").append("<option>5</option>")
}

function hidetext() {
    $("[type=button]").click(function(){
      var a = "test";
      console.log("a = " + a);
    debugger;
    $("#test").hide();
  });
}

function test() {
    $("input").focus(function(){
      var a = "test";
      console.log("a = " + a);
    debugger;
    $("#test").hide();
  });
}

function textalert() {
    $("#textalert").click(function () {
         var text = $("#test").text("aaabbbccc");
         debugger;
         alert("text: " + text);
         $("#test").addClass("test");
         $("#test").css({"font-size": "50px"});

    });
    
}