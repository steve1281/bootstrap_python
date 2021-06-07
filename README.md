# bootstrap-python

I got tired of re-creating the same directories and files over and over again.

So I wrote this.

## Clone

On a Mac:

```
 git clone https://github.com/steve1281/bootstrap_python.git
 cd bootstrap_python/
 pyenv local 3.9.1
 virtualenv virtualenv
 . ./virtualenv/bin/activate
 pip install -r requirements.txt
```

## Development Install

```
pip install -e .[test]

Sanity check:

(virtualenv) bigmac:bootstrap_python steve1281$ bootstrap_python --help
Usage: bootstrap_python [OPTIONS] PROJECT_NAME PROJECT_MAIN_FILE
                        PROJECT_MAIN_CLASS

  Build a skeleton python project. It will be deployed (by default) to the current
  folder. The project will need a name, a main file, and a main class.

Options:
  -d, --dryrun           Display commands that would be run instead of running
                         them

  -v, --debug            Set logging to debug
  -t, --target-dir TEXT  Targeted directory, assume CWD otherwise. (Will create if needed)
  --help                 Show this message and exit.
```

## Build

```
python -m build

(virtualenv) bigmac:bootstrap_python steve1281$ ls dist/
bootstrap_python-0.1.dev1+gb9cefa2-py3-none-any.whl
bootstrap_python-0.1.dev1+gb9cefa2.tar.gz

(virtualenv) bigmac:bootstrap_python steve1281$ unzip --content dist/bootstrap_python-0.1.dev1+gb9cefa2-py3-none-any.whl
caution:  both -n and -o specified; ignoring -o
Archive:  dist/bootstrap_python-0.1.dev1+gb9cefa2-py3-none-any.whl
    testing: bootstrap_python/__init__.py   OK
    testing: bootstrap_python/__main__.py   OK
    testing: bootstrap_python/bootstrap.py   OK
    testing: bootstrap_python/templates/README.md.template   OK
    testing: bootstrap_python/templates/__init__.py.template   OK
    testing: bootstrap_python/templates/__main__.py.template   OK
    testing: bootstrap_python/templates/project_main.py.template   OK
    testing: bootstrap_python/templates/requirements.txt.template   OK
    testing: bootstrap_python/templates/setup.py.template   OK
    testing: bootstrap_python/templates/test_project_main.py.template   OK
    testing: bootstrap_python-0.1.dev1+gb9cefa2.dist-info/METADATA   OK
    testing: bootstrap_python-0.1.dev1+gb9cefa2.dist-info/WHEEL   OK
    testing: bootstrap_python-0.1.dev1+gb9cefa2.dist-info/entry_points.txt   OK
    testing: bootstrap_python-0.1.dev1+gb9cefa2.dist-info/top_level.txt   OK
    testing: bootstrap_python-0.1.dev1+gb9cefa2.dist-info/RECORD   OK
No errors detected in compressed data of dist/bootstrap_python-0.1.dev1+gb9cefa2-py3-none-any.whl.

(virtualenv) bigmac:bootstrap_python steve1281$ deactivate
bigmac:bootstrap_python steve1281$ pip install dist/bootstrap_python-0.1.dev1+gb9cefa2-py3-none-any.whl
Processing ./dist/bootstrap_python-0.1.dev1+gb9cefa2-py3-none-any.whl
Installing collected packages: bootstrap-python
Successfully installed bootstrap-python-0.1.dev1+gb9cefa2
WARNING: You are using pip version 20.2.3; however, version 21.1.2 is available.
You should consider upgrading via the '/Users/steve1281/.pyenv/versions/3.9.1/bin/python3.9 -m pip install --upgrade pip' command.

```


## Usage

After doing the installation above, you can build a nice starter project:

```
cd ..

bigmac:Projects steve1281$ bootstrap_python sample_proj sample Sample -t sample_proj 
2021-06-05 18:44:00,554 - root - INFO   - project_name=sample_proj, project_name_file=sample, project_main_class=Sample, target_directory==sample_proj, dryrun=False, debug=False
2021-06-05 18:44:00,555 - root - INFO   - Created sample_proj/src.
2021-06-05 18:44:00,555 - root - INFO   - Created sample_proj/src/sample_proj.
2021-06-05 18:44:00,555 - root - INFO   - Created sample_proj/src/sample_proj/resources.
2021-06-05 18:44:00,555 - root - INFO   - Created sample_proj/test.
2021-06-05 18:44:00,559 - root - INFO   - Created sample_proj/README.md.
2021-06-05 18:44:00,560 - root - INFO   - Created sample_proj/src/sample_proj/__init__.py.
2021-06-05 18:44:00,561 - root - INFO   - Created sample_proj/test/__init__.py.
2021-06-05 18:44:00,563 - root - INFO   - Created sample_proj/src/sample_proj/__main__.py.
2021-06-05 18:44:00,564 - root - INFO   - Created sample_proj/src/sample_proj/sample.py.
2021-06-05 18:44:00,566 - root - INFO   - Created sample_proj/setup.py.
2021-06-05 18:44:00,567 - root - INFO   - Created sample_proj/requirements.txt.
2021-06-05 18:44:00,569 - root - INFO   - Created sample_proj/test/test_sample.py.

cd sample_proj
pyenv local 3.9.1
virtualenv virtualenv
git init
pip install -r requirements.txt
pip install -e .


bigmac:sample_proj steve1281$ sample_proj
Hello World

```

