import git
import os
import toml
from flask import Flask, abort, render_template
from flask_bootstrap import Bootstrap

with open('config.toml') as config_file:
    config = toml.loads(config_file.read())


def get_projects():
    projects = {}
    for project in os.listdir(config['projects_directory']):
        project_directory = os.path.join(config['projects_directory'], project)
        projects[project] = git.Repo(project_directory)
        projects[project].description = project # I'm not sure this is a good idea
    return projects

app = Flask(__name__)

bootstrap = Bootstrap()
bootstrap.init_app(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/projects', methods=['GET'])
def projects():
    projects = get_projects()
    return render_template('projects.html', projects=projects)


@app.route('/projects/<repo_name>', methods=['GET'])
def project(repo_name):
    projects = get_projects()
    project = projects.get(repo_name)
    if not project:
        return abort(404)
    return render_template('project.html', project=project)


if __name__ == '__main__':
    app.run(debug=True)
