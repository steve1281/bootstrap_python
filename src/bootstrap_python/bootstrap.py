import logging as log
import os
import sys
from pathlib import Path

from jinja2 import Template


def read_template(template):
    if not type(template) == str:
        return
    with open(template, 'r') as file:
        raw_data = file.read()
    if not raw_data:
        log.error(f"Not found: {template}")
        sys.exit(-1)
    return raw_data


class Bootstrap:
    def __init__(self, project_name,
                 project_main,
                 project_main_class,
                 target_directory,
                 dry_run=False):
        self.project_main = project_main
        self.project_name = project_name
        self.project_main_class = project_main_class
        self.target_directory = target_directory
        self.dry_run = dry_run

    def run(self):
        self.create_directories()
        self.create_readme()
        self.create_inits()
        self.create_main()
        self.create_base()
        self.create_setup()
        self.create_requirements()
        self.create_test()

    def create_directories(self):
        """
            $ mkdir src
            $ mkdir test
            $ mkdir src/proj_name
            $ mkdir src/proj_name/resources
        """
        self.create_directory(self.target_directory + '/src')
        self.create_directory(self.target_directory + '/src/' + self.project_name)
        self.create_directory(self.target_directory + '/src/' + self.project_name + "/resources")
        self.create_directory(self.target_directory + '/test')

    def create_directory(self, src_dir):
        if self.dry_run:
            log.info(f"Would have created/used: {src_dir}")
        else:
            Path(src_dir).mkdir(parents=True, exist_ok=True)
            log.info(f"Created {src_dir}.")

    def apply_template(self, output_file, template_data):
        t = Template(template_data)
        script = t.render(PROJECT_NAME=self.project_name,
                          PROJECT_MAIN=self.project_main,
                          PROJECT_MAIN_CLASS=self.project_main_class)
        if self.dry_run:
            log.info(f"Would have written {output_file}\n{script}")
        else:
            with open(output_file, "w") as f:
                f.write(script)
            log.info(f"Created {output_file}.")

    def create_readme(self):
        template_file = os.path.dirname(__file__) + "/templates/README.md.template"
        template_data = read_template(template_file)
        output_file = self.target_directory + "/README.md"
        self.apply_template(output_file, template_data)

    def create_inits(self):
        template_file = os.path.dirname(__file__) + "/templates/__init__.py.template"
        template_data = read_template(template_file)
        output_file = self.target_directory + '/src/' + self.project_name + '/' + '__init__.py'
        self.apply_template(output_file, template_data)
        output_file = self.target_directory + '/test/__init__.py'
        self.apply_template(output_file, template_data)

    def create_main(self):
        template_file = os.path.dirname(__file__) + "/templates/__main__.py.template"
        template_data = read_template(template_file)
        output_file = self.target_directory + '/src/' + self.project_name + '/' + '__main__.py'
        self.apply_template(output_file, template_data)

    def create_base(self):
        template_file = os.path.dirname(__file__) + "/templates/project_main.py.template"
        template_data = read_template(template_file)
        output_file = self.target_directory + '/src/' + self.project_name + "/" + self.project_main + ".py"
        self.apply_template(output_file, template_data)

    def create_setup(self):
        template_file = os.path.dirname(__file__) + "/templates/setup.py.template"
        template_data = read_template(template_file)
        output_file = self.target_directory + "/setup.py"
        self.apply_template(output_file, template_data)

    def create_requirements(self):
        template_file = os.path.dirname(__file__) + "/templates/requirements.txt.template"
        template_data = read_template(template_file)
        output_file = self.target_directory + "/requirements.txt"
        self.apply_template(output_file, template_data)

    def create_test(self):
        template_file = os.path.dirname(__file__) + "/templates/test_project_main.py.template"
        template_data = read_template(template_file)
        output_file = self.target_directory + "/test/test_" + self.project_main + ".py"
        self.apply_template(output_file, template_data)
