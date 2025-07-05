describe('Page d\'accueil', () => {
  it('affiche la liste des employés', () => {
    cy.visit('/');
    cy.contains('Liste des employés');
    cy.contains('Alice');
    cy.contains('Bob');
  });
});
