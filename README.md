# One Health Geography Data
This repo contains all geography data used for analysis and presentation of data, i.e.:
- Names and LGD codes and States, Districts, City Corporations, Wards, Sub-Districts and Villages
- Geojson Maps of all above-mentioned geographical entities

## Sources
- `sources/kgis`: https://kgis.ksrsac.in/kgis/downloads.aspx
- `sources/lgdirectory`: https://lgdirectory.gov.in/downloadDirectory.do
- `sources/datameet`: https://github.com/datameet/Pune_wards
- https://www.pcmcindia.gov.in/pdf/election2017/draft_ward/PCMC-2017%20DRAFT%20MAP.pdf

## Outputs
Data to be used is in the `output` folder:
- `output/ka_regions.json`: Geographical Entities in Karnataka State with name, LGD code, parent name, and parent LGD Code.
- `output/pcmc_regions.json`: Geographical Entities in Pimpri Chinchwad Muncipal Corporation with name, LGD code, parent name, and parent LGD Code.
- `output/maps`: Maps of geographical regions at an individual level, as well as with subregions in geojson format.
- `output/compressed_maps`: Compressed version of `output/maps`. Smaller in size, optimized for web loading, and to be used only for visual representation. DO NOT USE THIS FOR ANALYSIS.
- `output/maps/warnings.txt`: Since Map Data and Hierarchy Data were obtained from different source, there are some mismatches. Some regions have maps but are not in LGD, and vice-versa. Those regions are listed here.

## How to Run
The following instructions will generate usable files from `sources/` into the `output` folder
- The `./main.sh` bash script works only on Linux systems. Please run this only on Linux. 
- Create python venv under folder `venv/` and install python packages listed in `requirements.txt`.
- Make sure you have nodejs installed and the packages `mapshaper` and `geojson-rewind` are available on command line.
- Execute `./main.sh`.