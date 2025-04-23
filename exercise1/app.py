try:
    from nanodash import NanoDash
except ModuleNotFoundError:
    from exercise1.nanodash import NanoDash

# Create a new Flask web server
app = NanoDash()

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()