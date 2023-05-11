This repo contains all geography data used in the dashboards: Maps, Names and LGD codes

## Sources
- sources/kgis: https://kgis.ksrsac.in/kgis/downloads.aspx
- sources/lgdirectory: https://lgdirectory.gov.in/downloadDirectory.do
- sources/datameet: https://github.com/datameet/Pune_wards
- https://www.pcmcindia.gov.in/pdf/election2017/draft_ward/PCMC-2017%20DRAFT%20MAP.pdf

## How to Run
The following instructions will generate usable files from `sources/` into the `output` folder
- The `./main.sh` bash script works only on Linux systems. Please run this only on Linux. 
- Create python venv under folder `venv/` and install python packages listed in `requirements.txt`.
- Make sure you have nodejs installed and the packages `mapshaper` and `geojson-rewind` are available on command line.
- Execute `./main.sh`.