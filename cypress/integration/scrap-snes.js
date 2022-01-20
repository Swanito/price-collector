import Search from '../support/ebay-script';

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for SNES', () => {
        Search('SNES', './input-files/snes.json');
    });
});