in_options = {internalProjection: new OpenLayers.Projection('EPSG:900913'), externalProjection: new OpenLayers.Projection('EPSG:4326')}

to_district_vector = (wkt, ratio) ->
  format =  new OpenLayers.Format.WKT in_options
  feature = format.read wkt
  if ratio > 0.15
    feature.style = style_red
  else
    feature.style = style_blue
  feature

layer_style = OpenLayers.Util.extend({}, OpenLayers.Feature.Vector.style['default'])
layer_style.fillOpacity = 0.2;
layer_style.graphicOpacity = 1;
style_blue = OpenLayers.Util.extend({}, layer_style)
style_blue.strokeColor = "blue";
style_blue.fillColor = "blue";

style_red = OpenLayers.Util.extend({}, style_blue)
style_red.strokeColor = "red";
style_red.fillColor = "red";