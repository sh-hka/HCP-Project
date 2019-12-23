var results = [];

result_list = document.getElementById("results-list");

function showResult(result) {
  var item = document.createElement("div");
  item.classList.add("item");
  item.appendChild(getResultCard(result));
  result_list.appendChild(item);
  var position = { lat: result.lat, lng: result.lng };
  placeMarker(map, result.name, position, getResultCard(result));
}

function clearResults() {
  result_list.innerHTML = "";
  clearMarkers();
}

function getResultCard(result) {
  var result_container = document.createElement("div");
  result_container.classList.add("ui", "card", "result");
  var name_container = document.createElement("div");
  name_container.classList.add("content");
  result_container.appendChild(name_container);
  var name = document.createElement("div");
  name.classList.add("header");
  name.innerText = result.name;
  name_container.appendChild(name);

  var content = document.createElement("div");
  content.classList.add("content");
  result_container.appendChild(content);
  var feed = document.createElement("div");
  feed.classList.add("ui", "small", "feed");
  content.appendChild(feed);

  var event1 = document.createElement("div");
  event1.classList.add("event");
  feed.appendChild(event1);
  var event1content = document.createElement("div");
  event1content.classList.add("content");
  event1.appendChild(event1content);
  var summary1 = document.createElement("div");
  summary1.classList.add("summary");
  summary1.innerText = result.speciality;
  event1content.appendChild(summary1);

  var event2 = document.createElement("div");
  event2.classList.add("event");
  feed.appendChild(event2);
  var event2content = document.createElement("div");
  event2content.classList.add("content");
  event2.appendChild(event2content);
  var summary2 = document.createElement("div");
  summary2.classList.add("summary");
  var address =
    result.address + "," + result.city + "\n" + result.state + "," + result.zip;
  summary2.innerText = address;
  event2content.appendChild(summary2);

  var bttn_container = document.createElement("div");
  bttn_container.classList.add("extra", "content");
  result_container.appendChild(bttn_container);
  var bttn = document.createElement("button");
  bttn.classList.add("ui");
  bttn.classList.add("button");
  bttn.innerHTML = "Apply";
  bttn.onclick = function() {
    const url = "/apply?provider=" + id;
    window.location = url;
  };
  bttn_container.appendChild(bttn);

  return result_container;
}
