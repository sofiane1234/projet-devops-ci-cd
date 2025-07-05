const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://frontend-staging.azurewebsites.net',
    specPattern: 'cypress/e2e/**/*.cy.js',
    supportFile: false
  }
});
