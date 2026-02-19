from flask import render_template, abort, send_from_directory
from .registry import get_all_shops, find_shop
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOPS_PATH = os.path.join(BASE_DIR, "shops")


def register_routes(app):

    # ✅ Homepage – show ALL arts
    @app.route("/")
    def home():
        shops = get_all_shops()
        return render_template(
            "base.html",
            shops=shops,
            title="ShivArt"
        )

    # ✅ Individual Art Page
    @app.route("/art/<slug>")
    def art_page(slug):
        shop = find_shop(slug)
        if not shop:
            abort(404)

        return render_template(
            "art_page.html",
            shop=shop
        )

    # ✅ Preview Image
    @app.route("/preview/<slug>")
    def preview_image(slug):
        shop = find_shop(slug)
        if not shop:
            abort(404)

        folder = os.path.join(SHOPS_PATH, slug)
        return send_from_directory(folder, shop["preview"])

    # ✅ Download PDF
    @app.route("/download/<slug>")
    def download_file(slug):
        shop = find_shop(slug)
        if not shop:
            abort(404)

        folder = os.path.join(SHOPS_PATH, slug)
        return send_from_directory(
            folder,
            shop["file"],
            as_attachment=True
        )
