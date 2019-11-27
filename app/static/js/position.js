var currentPos = null;

function setCurrentPos(lat, lng) {
    currentPos = {
        lat: lat,
        lng: lng
    }
}

navigator.geolocation.getCurrentPosition(function (position) {
    setCurrentPos(position.coords.latitude, position.coords.longitude);
});
