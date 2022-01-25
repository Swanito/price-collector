import Search from '../support/ebay-script';

const initial = Cypress.env("INITIAL_INDEX") || 0;

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for PS1', () => {
        Search('Playstation 1', './input-files/ps1.json', initial);
    });
});