import json
import lxml.html
import os
import os.path

print("\nFORMATTING KGIS MAPS...")
warnings = ""
def _scrape_description_for_region_id(html_description):
    html = lxml.html.fromstring(html_description)
    td_list = html.xpath("//td")
    for i in range(len(td_list)):
        t = td_list[i].text_content()
        if t.startswith("LGD_VillageCode"):
            return "village_" + td_list[i+1].text_content()
        elif t.startswith("LGD_DistrictCode"):
            return "district_" + td_list[i+1].text_content()
        elif t.startswith("LGD_TalukCode"):
            return "subdistrict_" + td_list[i+1].text_content()
        elif t.startswith("KGISStateCode"):
            return "state_" + td_list[i+1].text_content()
        elif t=="KGISWardNo":
            return "ward_bbmp" + td_list[i+1].text_content()
    print(html_description)
    raise Exception("LGD NOT FOUND") 

DIR = "intermediates/kgis/"
OUTPUT_DIR = "output/maps/individual/"
KA_REGIONS = json.loads(open("output/ka_regions.json").read())

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(DIR):
    filepath = DIR + filename
    print("Processing", filepath)
    geo_obj = json.loads(open(filepath).read())
    
    if filepath.endswith("/bbmp.geojson"):
        region_id = "localbody_276600"
        new_feature = {
            "type": "Feature",
            "geometry": geo_obj["geometries"][0],
            "properties": KA_REGIONS[region_id]
        }
        new_obj = {
            "type": "FeatureCollection",
            "features": [new_feature],
        }
        outfile_path = OUTPUT_DIR + region_id + ".geojson" 
        with open(outfile_path, "w") as f:
            #print("Writing", outfile_path)
            f.write(json.dumps(new_obj))
            f.close()
        continue
    
    for feature in geo_obj["features"]:
        html_description = feature["properties"]["description"]["value"]
        region_id = _scrape_description_for_region_id(html_description)
        if region_id not in KA_REGIONS:
            warnings += "Not in LGD Hierarchy: " + feature["properties"]["name"] + f" ({filepath})\n"
            continue
            
        new_feature = {
            "type": "Feature",
            "geometry": feature["geometry"],
            "properties": KA_REGIONS[region_id]
        }
        new_obj = {
            "type": "FeatureCollection",
            "features": [new_feature],
        }
        
        outfile_path = OUTPUT_DIR + region_id + ".geojson" 
        with open(outfile_path, "w") as f:
            #print("Writing", outfile_path)
            f.write(json.dumps(new_obj))
            f.close()

parent_map = {}
for region_id in KA_REGIONS:
    obj = KA_REGIONS[region_id]
    if not os.path.exists(OUTPUT_DIR + region_id + ".geojson"):
        warnings += " ".join([
            "Map data not found for",
            region_id, obj["name"],
            "in", obj["parent"], obj["parent_name"]
        ]) + "\n"
    if obj["parent"]:
        if obj["parent"] not in parent_map:
            parent_map[obj["parent"]] = []
        parent_map[obj["parent"]].append(region_id)

SUBREGION_OUTPUT_DIR = "output/maps/subregions/"  
os.makedirs(SUBREGION_OUTPUT_DIR, exist_ok=True)

for region_id in parent_map:
    subregion_ids = parent_map[region_id]
    geo_obj = {"type": "FeatureCollection", "features": []}
    for subregion_id in subregion_ids:
        if os.path.exists(OUTPUT_DIR + subregion_id + ".geojson"):
            txt = open(OUTPUT_DIR + subregion_id + ".geojson").read()
            feature = json.loads(txt)["features"][0]
            geo_obj["features"].append(feature)
    with open(SUBREGION_OUTPUT_DIR + region_id + ".geojson", "w") as f:
        f.write(json.dumps(geo_obj))
        f.close()

with open("output/maps/warnings.txt", "w") as f:
    f.write(warnings)
    f.close()