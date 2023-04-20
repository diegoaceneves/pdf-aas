from flask import Flask, Response, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from paste.translogger import TransLogger
import pdfkit
import cherrypy
import json

app = Flask(__name__)

tmpfolder = "/tmp/"


@app.route("/pdf", methods=["POST"])
def pdf():
    config = pdfkit.configuration(wkhtmltopdf="/bin/wkhtmltopdf")
    doc = handle_request(config)
    return Response(doc, mimetype="application/pdf")


@app.route("/jpg", methods=["POST"])
def jpg():
    config = pdfkit.configuration(wkhtmltopdf="/bin/wkhtmltoimage")
    doc = handle_request(config)
    return Response(doc, mimetype="image/jpg")


def handle_request(config):
    options = {}
    options = request.values.getlist("options", type=float)

    if "url" in request.get_json():
        print("URL provided: " + request.get_json()['url'])
        pdf = pdfkit.from_url(
            str(request.get_json()['url']),
            output_path=False,
            configuration=config,
            options=options,
        )

    if "html" in request.get_json():
        print("Html provided")
        pdf = pdfkit.from_string(
            request.get_json()["html"],
            output_path=False,
            configuration=config,
            options=options,
        )

    return pdf


def run_server():
    app_logged = TransLogger(app)
    cherrypy.tree.graft(app_logged, "/")
    cherrypy.config.update(
        {
            "engine.autoreload_on": True,
            "log.screen": True,
            "server.socket_port": 80,
            "server.socket_host": "0.0.0.0",
        }
    )
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    run_server()
