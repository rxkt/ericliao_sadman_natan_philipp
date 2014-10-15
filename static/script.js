var timeSinceLastTyped = -1;
$(document).ready(function() {
    setInterval(checkTimeSinceLastTyped, 100);
    $(".search-bar").on("input", function() {
        timeSinceLastTyped = 0;
        $(".spinner").hide();
        $(".answer").fadeOut(500);
    } );

    $(".home-search-bar").submit(function() {
        if ($("#ajax-checkbox").is(":checked")) {
            sendQuery();
        }
    } );
} );

function checkTimeSinceLastTyped() {
    if (timeSinceLastTyped == -1)
        return;

    timeSinceLastTyped += 100;
    if (timeSinceLastTyped > 1000)
        sendQuery();
    console.log(timeSinceLastTyped);
}

function sendQuery() {
    if (! $("#ajax-checkbox").is(":checked"))
        return;

    timeSinceLastTyped = -1;
    $(".spinner").fadeIn(1000);
    $(".answer").hide();

    var query = $(".search-bar").val();
    $.post("/search", { query : query }, function(results) {
        updateResults(results);
    } );
    return false;
}

function updateResults(results) {
    $(".spinner").hide(); 
    if (results.length > 100)
        $(".answer").addClass("long-answer");
    else
        $(".answer").removeClass("long-answer");
    
    $(".answer").show();

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
