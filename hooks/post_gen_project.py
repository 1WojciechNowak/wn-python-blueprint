import shutil

if "{{ cookiecutter.include_jupyter }}" != "yes":
    shutil.rmtree("notebooks")
