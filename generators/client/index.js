
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
