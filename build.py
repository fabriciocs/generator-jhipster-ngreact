import os
import shutil
import subprocess

# Define necessary directories
directories = [
    "generators",
    "generators/app",
    "generators/client",
    "generators/entity-client",
    "generators/client/templates/src/main/webapp/app/modules/login",
    "generators/client/templates/src/main/webapp/app/entities",
    "generators/client/templates/src/main/webapp/app/shared/layout/header"
]

# Create directories if they do not exist
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Write the contents of each `index.js` file to their respective locations
app_index_content = """
const Generator = require('yeoman-generator');

module.exports = class extends Generator {
    initializing() {
        this.composeWith(require.resolve('generator-jhipster/generators/app'));
    }

    writing() {
        // Add custom files and templates here
    }

    install() {
        this.installDependencies({
            bower: false,
            npm: true,
            yarn: true
        });
    }
};
"""
with open("generators/app/index.js", "w") as f:
    f.write(app_index_content)

client_index_content = """
const Generator = require('yeoman-generator');

module.exports = class extends Generator {
    initializing() {
        this.composeWith(require.resolve('generator-jhipster/generators/client'));
    }

    writing() {
        // Copy the customized templates for Material-UI
        this.fs.copyTpl(
            this.templatePath('src/main/webapp/app/**'),
            this.destinationPath('src/main/webapp/app'),
            this
        );
    }
};
"""
with open("generators/client/index.js", "w") as f:
    f.write(client_index_content)

entity_client_index_content = """
const Generator = require('yeoman-generator');

module.exports = class extends Generator {
    initializing() {
        this.composeWith(require.resolve('generator-jhipster/generators/entity-client'));
    }

    writing() {
        // Copy the customized entity templates for Material-UI
        this.fs.copyTpl(
            this.templatePath('src/main/webapp/app/entities/**'),
            this.destinationPath('src/main/webapp/app/entities'),
            this
        );
    }
};
"""
with open("generators/entity-client/index.js", "w") as f:
    f.write(entity_client_index_content)

# Define source directories
source_dirs = [
    "ai-gen",
    "ai-gen/entities",
    "ai-gen/headers"
]

# Define a dictionary for file mapping
file_mapping = {
    "account.tsx.ejs": "generators/client/templates/src/main/webapp/app/modules/account",
    "admin.tsx.ejs": "generators/client/templates/src/main/webapp/app/modules/admin",
    "entities.tsx.ejs": "generators/client/templates/src/main/webapp/app/modules/entities",
    "header.tsx.ejs": "generators/client/templates/src/main/webapp/app/shared/layout/header",
    "index.tsx.ejs": "generators/client/templates/src/main/webapp/app/modules/index",
    "menu.tsx.ejs": "generators/client/templates/src/main/webapp/app/shared/layout/menus",
    "validated-form.spec.tsx.ejs": "generators/client/templates/src/main/webapp/app/shared/util",
    "validated-form.tsx.ejs": "generators/client/templates/src/main/webapp/app/shared/util",
    "entity-detail.tsx.ejs": "generators/client/templates/src/main/webapp/app/entities/entity-detail",
    "entity-list.tsx.ejs": "generators/client/templates/src/main/webapp/app/entities/entity-list",
    "entity-update.tsx.ejs": "generators/client/templates/src/main/webapp/app/entities/entity-update"
}

# Function to move files
def move_files(source_dir, file_mapping):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file in file_mapping:
                destination_dir = file_mapping[file]
                destination_path = os.path.join(destination_dir, file)
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                shutil.move(os.path.join(root, file), destination_path)
                print(f"Moved {file} to {destination_path}")
            else:
                print(f"No mapping found for {file}")

# Move files from source directories to destination directories
for source_dir in source_dirs:
    move_files(source_dir, file_mapping)

# Initialize a new Git repository and commit changes
subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Initial commit of JHipster Material-UI blueprint"], check=True)
subprocess.run(["git", "remote", "add", "origin", "https://github.com/fabriciocs/generator-jhipster-ngreact.git"], check=True)
subprocess.run(["git", "push", "-u", "origin", "master"], check=True)
