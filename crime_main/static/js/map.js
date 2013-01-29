// Generated by CoffeeScript 1.3.3
var in_options, layer_style, style_blue, style_green, style_orange, style_red, style_red1, style_red2, style_yellow, to_district_vector;

in_options = {
  internalProjection: new OpenLayers.Projection('EPSG:900913'),
  externalProjection: new OpenLayers.Projection('EPSG:4326')
};

to_district_vector = function(wkt, ratio) {
  var feature, format;
  format = new OpenLayers.Format.WKT(in_options);
  feature = format.read(wkt);
  if (ratio < 0.05) {
    feature.style = style_green;
  }
  if (ratio > 0.05) {
    feature.style = style_yellow;
  }
  if (ratio > 0.10) {
    feature.style = style_orange;
  }
  if (ratio > 0.15) {
    feature.style = style_red;
  }
  if (ratio > 0.20) {
    feature.style = style_red1;
  }
  if (ratio > 0.25) {
    feature.style = style_red2;
  }
  return feature;
};

layer_style = OpenLayers.Util.extend({}, OpenLayers.Feature.Vector.style['default']);

layer_style.fillOpacity = 0.2;

layer_style.graphicOpacity = 1;

style_blue = OpenLayers.Util.extend({}, layer_style);

style_blue.strokeColor = "blue";

style_blue.fillColor = "blue";

style_green = OpenLayers.Util.extend({}, style_blue);

style_green.strokeColor = "green";

style_green.fillColor = "green";

style_green.fillOpacity = "0.4";

style_red = OpenLayers.Util.extend({}, style_blue);

style_red.strokeColor = "red";

style_red.fillColor = "red";

style_red.fillOpacity = "0.4";

style_red1 = OpenLayers.Util.extend({}, style_blue);

style_red1.strokeColor = "red";

style_red1.fillColor = "red";

style_red1.fillOpacity = "0.7";

style_red2 = OpenLayers.Util.extend({}, style_blue);

style_red2.strokeColor = "red";

style_red2.fillColor = "red";

style_red2.fillOpacity = "1";

style_yellow = OpenLayers.Util.extend({}, style_blue);

style_yellow.strokeColor = "yellow";

style_yellow.fillColor = "yellow";

style_yellow.fillOpacity = "0.4";

style_orange = OpenLayers.Util.extend({}, style_blue);

style_orange.strokeColor = "orange";

style_orange.fillColor = "orange";

style_orange.fillOpacity = "0.4";
