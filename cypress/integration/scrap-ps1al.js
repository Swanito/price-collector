import Search from '../support/ebay-script';

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for PS1 AL', () => {
        Search('Playstation 1', './input-files/ps1al.json');
    });
});