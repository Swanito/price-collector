import Search from '../support/ebay-script';

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for SEGA Dreamcast', () => {
        Search('SEGA Dreamcast', './input-files/dc.json');
    });
});