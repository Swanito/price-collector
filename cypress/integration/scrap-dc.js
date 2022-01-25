import Search from '../support/ebay-script';

const initial = Cypress.env("INITIAL_INDEX") || 0;

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for SEGA Dreamcast', () => {
        Search('SEGA Dreamcast', './input-files/dc.json', initial);
    });
});