mkdir -p output

venv/bin/python3 generate_hierarchy.py
./convert_kgis_maps.sh
venv/bin/python3 format_maps.py
./generate_compressed_maps.sh