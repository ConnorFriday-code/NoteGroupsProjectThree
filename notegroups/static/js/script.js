$(document).ready(function(){
    $("#menu-button").click(function(event){
        if ($("#dropdown-list").css("display") == "none"){
            $("#dropdown-list").css("display", "block")
        }
        else{
            $("#dropdown-list").css("display", "none")
        }
    })
})