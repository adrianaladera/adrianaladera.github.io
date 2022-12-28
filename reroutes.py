# import sys
# from flask import Flask, render_template
# from flask_flatpages import FlatPages
# from flask_frozen import Freezer 

# DEBUG = True
# FLATPAGES_AUTO_RELOAD = DEBUG
# FLATPAGES_EXTENSION = '.md'

# app = Flask(__name__)
# app.config.from_object(__name__)
# pages = FlatPages(app)
# freezer = Freezer(app)
  
# # Pass the required route to the decorator.
# @app.route('/')
# def index():
#     return render_template('home.html', pages=pages)

# @app.route("/research")
# def research():
#     return render_template("research.html", pages=pages)

# @app.route("/experience")
# def experience():
#     return render_template("experience.html", pages=pages)

# @app.route("/play")
# def play():
#     return render_template("play.html", pages=pages)

# @app.route("/other-sites")
# def other_sites():
#     return render_template("sites.html", pages=pages)

# # if __name__ == '__main__':
# #     app.run(debug=True, host='0.0.0.0', port=5000)

# if __name__ == "__main__":
#     if len(sys.argv) > 1 and sys.argv[1] == "build":
#         freezer.freeze()
#     else:
#         app.run()

# # if __name__ == "__main__":
# #     app.run()