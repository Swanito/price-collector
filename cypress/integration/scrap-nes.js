import Search from '../support/ebay-script';

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for NES', () => {
        Search('NES', './input-files/nes.json');
    });
});