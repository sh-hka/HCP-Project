
const search_bar = document.getElementById("search-bar");

// Init the SearchBar actions
function initSearchBar() {
    search_bar.onkeydown = function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            search_bar.blur();
            search(search_bar);
        }
    };
}

function search() {
    console.log('search()');
    const query_string = search_bar.querySelector('#query').value;
    const cLatLng = currentPos;
    var range = 30; // Stub
    const range_option = search_bar.querySelector('#search_range');
    if (range_option !== null) {
        const range = range_option.value;
    }
    var query = JSON.stringify({query: query_string, position: cLatLng, range: range});
    // Now construct the query url:
    const url = '/search?data=' + encodeURIComponent(query);
    window.location = url;
}
