const dateFormat = require('dateformat');

const search = (platformName, fileUrl, initialIndex = 0) => {
    cy.task('log', `STARTING INDEX ${initialIndex}`);

    const timestamp = Date.now();
    const date = dateFormat(timestamp, 'dd-mm-yyyy');
    const gameModel = { game: null, platform: platformName, adTitle: null, secondaryInfo: null, price: null, shipping: null, sellingDate: null, location: null, sampleTimestamp: timestamp, sampleDate: date };
    const gameArray = [];
    const waitTime = 50;

    cy.visit('https://www.ebay.es/');

    cy.readFile(fileUrl).then(async (games) => {
        for (let i = initialIndex; i <= games.games.length; i++) {
            const game = games.games[i];
            cy.findMany({ game, sampleDate: date }, 'games', 'testdb').then((res) => {
                cy.task('log', `IS GAME STORED ${res.length > 0}`);
                if (res.length === 0) {
                    gameModel.game = game;
                    const fullCriteria = `${platformName} ${game}`;
                    //search
                    cy.task('log', `CHECKING ${game}`);
                    cy.get('#gh-ac').clear().type(fullCriteria, { force: true });
                    cy.get('#gh-btn').click();
                    //filter by country
                    cy.get(
                        '#x-refine__group__4 > .x-refine__main__value > :nth-child(4)',
                    ).click();
                    //filter by sold
                    cy.get(
                        '.x-refine__main__value > [name="LH_Sold"]',
                    ).click();

                    //iterate over the list
                    cy.get('#srp-river-results > ul').each(($list) => {
                        cy.wrap($list).within(() => {
                            if ($list.find('li.s-item').length) {
                                cy.get('li.s-item').each(($listItem) => {
                                    cy.wrap($listItem).within(() => {
                                        //get the title
                                        cy.get('.s-item__title').then((gameTitle) => {
                                            //check if title includes the game
                                            const titleText = gameTitle.text();
                                            if (titleText.includes(game)) {
                                                gameModel.adTitle = titleText;
                                                //get the price
                                                if ($listItem.find('.s-item__price').length) {
                                                    cy.wait(waitTime);
                                                    cy.get('.s-item__price').then((gamePrice) => {
                                                        gameModel.price = gamePrice.text();
                                                    });
                                                }
                                                //get the shipping cost
                                                if ($listItem.find('.s-item__shipping').length) {
                                                    cy.wait(waitTime);
                                                    cy.get('.s-item__shipping').then((gameShipping) => {
                                                        gameModel.shipping = gameShipping.text();
                                                    });
                                                }
                                                //get the secondary info
                                                if ($listItem.find('div.s-item__subtitle > span.SECONDARY_INFO').length) {
                                                    cy.wait(waitTime);
                                                    cy.get('div.s-item__subtitle > span.SECONDARY_INFO').then((secondaryInfo) => {
                                                        gameModel.secondaryInfo = secondaryInfo.text();
                                                    });
                                                }                                                
                                                //get the selling date
                                                if ($listItem.find('.s-item__title--tagblock > span.POSITIVE').length) {
                                                    cy.wait(waitTime);
                                                    cy.get('.s-item__title--tagblock > span.POSITIVE').then((gameDate) => {
                                                        gameModel.sellingDate = gameDate.text();
                                                    });
                                                }
                                                //get location
                                                if ($listItem.find('.s-item__location').length) {
                                                    cy.wait(waitTime);
                                                    cy.get('.s-item__location').then((gameLocation) => {
                                                        gameModel.location = gameLocation.text();
                                                    });
                                                }

                                                gameModel.game = game;
                                                if (!gameArray.includes(gameModel)) {
                                                    gameArray.push(gameModel);
                                                }
                                                cy.insertMany(gameArray, 'games', 'testdb').then(res => {
                                                    cy.task('log', `${JSON.stringify(res)} STORED`);
                                                });
                                            }
                                        });
                                    });
                                });
                            }
                        });

                    });

                }
            });
        }
    });
};

export default search;