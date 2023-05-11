echo
echo "GENERATING COMPRESSED MAPS..."
mkdir -p output/compressed_maps/individual/
mkdir -p output/compressed_maps/subregions/
rm output/compressed_maps/individual/*
rm output/compressed_maps/subregions/*

for filepath in $(find output/maps/ -name '*.geojson'); do
  targetfilepath="${filepath/\/maps\//\/compressed_maps\/}"
  mapshaper -i $filepath -simplify 1% -o $targetfilepath format=geojson 
done