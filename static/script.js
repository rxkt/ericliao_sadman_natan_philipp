$(document).ready(function() {
    $(".search-bar").on("input", function() {
        if (! $("#ajax-checkbox").is(":checked"))
            return;

        $(".spinner").fadeIn(1000);

        var query = $(this).val();
        $.post("/search", { query : query }, function(results) {
            updateResults(results);
        } );
    } );

    $(".home-search-bar").submit(function() {
        if ($("#ajax-checkbox").is(":checked"))
            return false;
    } );
} )

function updateResults(results) {
    $(".spinner").hide(); 
    if (results.length > 100)
        $(".answer").addClass("long-answer");
    else
        $(".answer").removeClass("long-answer");

    $(".answer").text(results);
    var query = $(".search-bar").val();
    window.history.pushState({}, "", "/search?query=" + encodeURIComponent(query));
}

// Back button
window.onpopstate = function(e){
    if(e.state){
        document.getElementById("content").innerHTML = e.state.html;
        document.title = e.state.pageTitle;
    }
};
