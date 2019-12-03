// Default startup location
var currentPos = {
    lat: 39.90,
    lng: -75.2
};

function setCurrentPos(lat, lng) {
    currentPos = {
        lat: lat,
        lng: lng
    }
}

navigator.geolocation.getCurrentPosition(function (position) {
    setCurrentPos(position.coords.latitude, position.coords.longitude);
});
