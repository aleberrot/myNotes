'''
This module is for initializating the app
'''
from website import create_app, create_database # Getting the create_app function from the website package

app = create_app() 
if __name__ == '__main__':
    create_database(app)
    app.run(debug=True) # Running the app on debug mode