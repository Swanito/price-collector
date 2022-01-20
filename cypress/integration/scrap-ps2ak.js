import Search from '../support/ebay-script';

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for PS2 AK', () => {
        Search('Playstation 2', './input-files/ps2ak.json');
    });
});