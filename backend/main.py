from .app import create_app  # Import the function to create the Flask app

# Call the create_app function to get the Flask app
app = create_app()

# If this script is run directly, start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)