var mapOptions = {
    center: [44.80446, 20.46578],
    zoom: 15
}
    
var map = new L.map('map', mapOptions);

var layer = new L.TileLayer(`http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`);

map.addLayer(layer);