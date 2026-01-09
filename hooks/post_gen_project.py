import shutil

if "{{ cookiecutter.include_tests }}" != "yes":
    shutil.rmtree("tests")

if "{{ cookiecutter.include_jupyter }}" != "yes":
    shutil.rmtree("notebooks")
