$(document).ready(function(){

    //Dropdown nav menu for mobile on click
    $("#menu-button").click(function(event){
        //Swap between hidden and displayed
        if ($("#dropdown-list").css("display") == "none"){
            $("#dropdown-list").css("display", "block")
        }
        else{
            $("#dropdown-list").css("display", "none")
        }
    })

    //Grabbing of id and title to fill delete pop-up
    $(".delete-button").click(function(){
        //Grab note id
        var noteId = $(this).data("note-id")
        //Brab note title
        var noteTitle = $(this).data("note-title")
        //Fill title section with the grabbed title
        $("#delete-check-title").text(noteTitle)
        //On selecting confirm delete, delete note with grabbed id
        $("#confirm-delete").attr("href", "/delete_note/"+noteId)

        //Toggle delete pop-up to visible
        $("#delete-check-outer").toggleClass("hidden visible")
    })

    //Toggle delete pop-up to hidden
    $("confirm-delete").click(function(){
        $("#delete-check-outer").toggleClass("hidden visible")
    })

    //Toggle delete pop-up to hidden
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