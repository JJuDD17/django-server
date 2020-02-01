var index = 0

console.log(index)
function buttonClicked1(){
    index += 1
    console.log(index)
    $("#index").val(index)
    $("#div1").html(index)
    var oldContent = $("#div1").html()
    $("#div1").html(oldContent + "<div class='bg'></div>")
}

function buttonClicked2(){
    self = $("#btn-active")
    self.attr("id", "btn-inactive")
    self.attr("class", "btn btn-danger")
    self.attr("onclick", "alert('!!!!!')")
    self.text("DON'T CLICK ME")

    old = $(".bg-div").html()
    $(".bg-div").html(old + '<button class="btn btn-primary" onclick="buttonClicked2()" id="btn-active">CLICK ME</button>')
}