from nanodash.nanodash import NanoDash

# Create a new Flask web server
app = NanoDash()

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()