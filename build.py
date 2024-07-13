import os
import shutil

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
    os.makedirs(directory, exist_ok=True)

# Write the contents of each `index.js` file to their respective locations
def write_index_file(path, content):
    with open(path, "w") as f:
        f.write(content)

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
write_index_file("generators/app/index.js", app_index_content)

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
write_index_file("generators/client/index.js", client_index_content)

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
write_index_file("generators/entity-client/index.js", entity_client_index_content)

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
    "entity-update.tsx.ejs": "generators/client/templates/src/main/webapp/app/entities/entity-update",
    "login-modal.tsx.ejs": "generators/client/templates/src/main/webapp/app/modules/login",
    "login-redirect.tsx.ejs": "generators/client/templates/src/main/webapp/app/modules/login",
    "login.tsx.ejs": "generators/client/templates/src/main/webapp/app/modules/login",
    "logout.tsx.ejs": "generators/client/templates/src/main/webapp/app/modules/login"
}

# Function to move files
def move_files(source_dir, file_mapping):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file in file_mapping:
                destination_dir = file_mapping[file]
                destination_path = os.path.join(destination_dir, file)
                os.makedirs(destination_dir, exist_ok=True)
                shutil.move(os.path.join(root, file), destination_path)
                print(f"Moved {file} to {destination_path}")
            else:
                print(f"No mapping found for {file}")

# Move files from source directories to destination directories
for source_dir in source_dirs:
    move_files(source_dir, file_mapping)
