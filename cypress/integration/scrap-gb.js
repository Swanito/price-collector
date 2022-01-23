import Search from '../support/ebay-script';

const initial = Cypress.env("INITIAL_INDEX") || 0;

describe('ebay', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        return false;
    });

    it('Searches for Game Boy', () => {
        Search('Game Boy', './input-files/game-boy.json', initial);
    });
});