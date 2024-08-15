from nanodash.nanodash import NanoDash

# Create a new Flask web server
app = NanoDash()

app.set_layout('<h1>Hello, World!</h1>')

app.run()