echo
echo "CONVERTING KGIS MAPS TO GEOJSON"
mkdir -p intermediates/kgis
rm intermediates/kgis/*
for filepath in sources/kgis/*.kmz; do
  filename="$(basename $filepath .kmz)"
  mapshaper -i $filepath -o intermediates/kgis/$filename.raw.geojson format=geojson
  echo "Rewinding $filename.raw.geojson to $filename.geojson"
  geojson-rewind --counterclockwise intermediates/kgis/$filename.raw.geojson > intermediates/kgis/$filename.geojson
  rm intermediates/kgis/$filename.raw.geojson
done
mapshaper -i sources/kgis/2003_BBMP.kmz -dissolve -o intermediates/kgis/bbmp.raw.geojson format=geojson
echo "Rewinding bbmp.raw.geojson to bbmp.geojson"
geojson-rewind --counterclockwise intermediates/kgis/bbmp.raw.geojson > intermediates/kgis/bbmp.geojson  
rm intermediates/kgis/bbmp.raw.geojson
