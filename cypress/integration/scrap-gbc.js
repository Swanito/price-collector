import Search from '../support/ebay-script';

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for Game Boy Color', () => {
        Search('Game Boy Color', './input-files/game-boy-color.json');
    });
});