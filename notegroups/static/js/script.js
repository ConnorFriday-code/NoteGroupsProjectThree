$(document).ready(function(){

    //Dropdown nav menu for mobile
    $("#menu-button").click(function(event){
        if ($("#dropdown-list").css("display") == "none"){
            $("#dropdown-list").css("display", "block")
        }
        else{
            $("#dropdown-list").css("display", "none")
        }
    })

    //Grabbing of id and title to fill delete pop-up
    $(".delete-button").click(function(){
        var noteId = $(this).data("note-id")
        var noteTitle = $(this).data("note-title")
        $("#delete-check-title").text(noteTitle)
        $("#confirm-delete").attr("href", "/delete_note/"+noteId)

        $("#delete-check-outer").toggleClass("hidden visible")
    })

    $("confirm-delete").click(function(){
        $("#delete-check-outer").toggleClass("hidden visible")
    })

    $("#cancel-delete").click(function(){
        $("#delete-check-outer").toggleClass("hidden visible")
    })

    //Search function on home page
    $("#search-input").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".note-card").filter(function() {
            $(this).toggle($(this).find(".card-title").text().toLowerCase().indexOf(value) > -1 ||
                           $(this).find(".card-description").text().toLowerCase().indexOf(value) > -1);
        });
    });
})