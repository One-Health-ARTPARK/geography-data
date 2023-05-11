import json
import os
import parse_lgd_html

print("\nGENERATING HIERARCHY JSON...")

LGD_DIR = "sources/lgdirectory/"
os.makedirs("output/", exist_ok=True)

KA_REGIONS = {
    "state_29": {
        "region_id": "state_29",
        "name": "KARNATAKA",
        "parent": "",
        "parent_name": "",
    }
}

print("Reading KA Districts")
ka_districts = parse_lgd_html.parse(LGD_DIR+"ka-districts.htm")
for d in ka_districts:
    region_id = "district_" + d["District Code"]
    KA_REGIONS[region_id] = {
        "region_id": region_id,
        "name": d["District Name(In English)"].upper(),
        "parent": "state_29",
        "parent_name": KA_REGIONS["state_29"]["name"]
    }

print("Reading BBMP Wards")
bbmp_region_id = "localbody_276600"
bbmp_lgd = "276600"
KA_REGIONS[bbmp_region_id] = {
    "region_id": bbmp_region_id,
    "name": "BBMP",
    "parent": "state_29",
    "parent_name": KA_REGIONS["state_29"]["name"]
}

ka_wards = parse_lgd_html.parse(LGD_DIR+"ka-wards.htm")
for w in ka_wards:
    if w["Local Body Code"]==bbmp_lgd:
        region_id = "ward_bbmp" + w["\xa0Ward Number"]
        parent = bbmp_region_id
        KA_REGIONS[region_id] = {
            "region_id": region_id,
            "name": w["Ward Name"].upper(),
            "parent": parent,
            "parent_name": KA_REGIONS[parent]["name"]
        }

print("Reading KA Sub-districts")
ka_subdistricts = parse_lgd_html.parse(LGD_DIR+"ka-subdistricts.htm")
for s in ka_subdistricts:
    region_id = "subdistrict_" + s["Subdistrict Code"]
    parent = "district_" + s["District code"]
    KA_REGIONS[region_id] = {
        "region_id": region_id,
        "name": s["Subdistrict Name\xa0\xa0(In English)"].upper(),
        "parent": parent,
        "parent_name": KA_REGIONS[parent]["name"]
    }

print("Reading KA Villages")
ka_villages = parse_lgd_html.parse(LGD_DIR+"ka-villages.htm")
for v in ka_villages:
    region_id = "village_" + v["Village Code"]
    parent = "subdistrict_" + v["Sub-District Code"]
    KA_REGIONS[region_id] = {
        "region_id": region_id,
        "name": v["Village Name\xa0(In English)"].upper(),
        "parent": parent,
        "parent_name": KA_REGIONS[parent]["name"]
    }
        
output = json.dumps(KA_REGIONS, indent=2)
with open("output/ka_regions.json", "w") as f:
    f.write(output)
    f.close()

print("Reading PCMC Wards")
pcmc_region_id = "localbody_251528"
pcmc_lgd = "251528"

PCMC_REGIONS = {
    pcmc_region_id: {
        "region_id": pcmc_region_id,
        "name": "PCMC",
        "parent": "",
        "parent_name": ""
    }
}

mh_wards = parse_lgd_html.parse(LGD_DIR+"mh-wards.htm")
for w in mh_wards:
    if w["Local Body Code"]==pcmc_lgd:
        region_id = "ward_pcmc" + w["\xa0Ward Number"]
        parent = pcmc_region_id
        PCMC_REGIONS[region_id] = {
            "region_id": region_id,
            "name": "Ward No. " + w["\xa0Ward Number"],
            "parent": parent,
            "parent_name": PCMC_REGIONS[parent]["name"]
        }

output = json.dumps(PCMC_REGIONS, indent=2)
with open("output/pcmc_regions.json", "w") as f:
    f.write(output)
    f.close()

