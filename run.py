from building.server import create_building

app = create_building()

if __name__ == "__main__":
    app.run(debug=True, port=5050)
