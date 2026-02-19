import os
import json

SHOPS_PATH = "shops"


def get_all_shops():
    shops = []

    if not os.path.exists(SHOPS_PATH):
        return shops

    for slug in sorted(os.listdir(SHOPS_PATH)):  # 🔥 sorted added
        shop_folder = os.path.join(SHOPS_PATH, slug)

        if not os.path.isdir(shop_folder):
            continue

        manifest = os.path.join(shop_folder, "shop.manifest.json")

        if os.path.exists(manifest):
            with open(manifest, "r", encoding="utf-8") as f:
                data = json.load(f)
                data["slug"] = slug
                shops.append(data)

    return shops


def find_shop(slug):
    for shop in get_all_shops():
        if shop.get("slug") == slug:
            return shop
    return None
