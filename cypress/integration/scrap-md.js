import Search from '../support/ebay-script';

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for Mega Drive', () => {
        Search('Mega Drive', './input-files/mega-drive.json');
    });
});