import os

def create_folder_structure():
    # Create project folder
    os.mkdir("fastapi-project")
    os.chdir("fastapi-project")

    # Create subfolders and files
    os.mkdir("alembic")
    os.mkdir("src")
    os.chdir("src")

    # Auth folder
    os.mkdir("auth")
    os.chdir("auth")
    open("router.py", "a").close()
    open("schemas.py", "a").close()
    open("models.py", "a").close()
    open("dependencies.py", "a").close()
    open("config.py", "a").close()
    open("constants.py", "a").close()
    open("exceptions.py", "a").close()
    open("service.py", "a").close()
    open("utils.py", "a").close()
    os.chdir("..")

    # Products folder
    os.mkdir("products")
    os.chdir("products")
    open("router.py", "a").close()
    open("schemas.py", "a").close()
    open("models.py", "a").close()
    open("dependencies.py", "a").close()
    open("constants.py", "a").close()
    open("exceptions.py", "a").close()
    open("service.py", "a").close()
    open("utils.py", "a").close()
    os.chdir("..")

    # Orders folder
    os.mkdir("orders")
    os.chdir("orders")
    open("router.py", "a").close()
    open("schemas.py", "a").close()
    open("models.py", "a").close()
    open("dependencies.py", "a").close()
    open("constants.py", "a").close()
    open("exceptions.py", "a").close()
    open("service.py", "a").close()
    open("utils.py", "a").close()
    os.chdir("..")

    # Main folder
    open("config.py", "a").close()
    open("models.py", "a").close()
    open("exceptions.py", "a").close()
    open("pagination.py", "a").close()
    open("database.py", "a").close()
    open("main.py", "a").close()
    os.chdir("..")

    # Tests folder
    os.mkdir("tests")
    os.chdir("tests")
    os.mkdir("auth")
    os.mkdir("products")
    os.mkdir("orders")
    os.chdir("..")

    # Templates folder
    os.mkdir("templates")
    os.chdir("templates")
    open("index.html", "a").close()
    os.chdir("..")

    # Requirements folder
    os.mkdir("requirements")
    os.chdir("requirements")
    open("base.txt", "a").close()
    open("dev.txt", "a").close()
    open("prod.txt", "a").close()
    os.chdir("..")

    # Create other files
    open(".env", "a").close()
    open(".gitignore", "a").close()
    open("logging.ini", "a").close()
    open("alembic.ini", "a").close()

if __name__ == '__main__':
    create_folder_structure()
