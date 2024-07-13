
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
