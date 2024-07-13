const Generator = require('yeoman-generator');

module.exports = class extends Generator {
  initializing() {
    this.composeWith(require.resolve('generator-jhipster/generators/app'));
  }

  writing() {
    // Add custom files and templates here if needed
  }

  install() {
    this.installDependencies({
      bower: false,
      npm: true,
      yarn: true
    });
  }
};
