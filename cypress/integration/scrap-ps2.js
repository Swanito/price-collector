import Search from '../support/ebay-script';

const initial = Cypress.env("INITIAL_INDEX") || 0;

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for PS2', () => {
        Search('Playstation 2', './input-files/ps2.json', initial);
    });
});