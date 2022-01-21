const dateFormat = require('dateformat');

const search = (platformName, fileUrl) => {
    const timestamp = Date.now();
    const date = dateFormat(timestamp, 'dd-mm-yyyy');
    const gameModel = { game: null, platform: platformName, adTitle: null, price: null, shipping: null, sellingDate: null, location: null, sampleTimestamp: timestamp, sampleDate: date };
    const gameArray = [];
    const waitTime = 50;


    cy.readFile(fileUrl).then(async (games) => {
        for (const key in games.games) {
            const game = games.games[key];
            cy.findMany({ game, sampleDate: date }, 'games', 'testdb').then((res) => {
                if (res.length === 0) {
                    gameModel.game = game;
                    const fullCriteria = `${platformName} ${game}`;
                    cy.visit(`https://www.ebay.es/sch/i.html?_nkw=${fullCriteria.replaceAll(' ', '\+')}&LH_PrefLoc=1&LH_Sold=1&LH_Complete=1&rt=nc&LH_All=1`);
                    //iterate over the list
                    cy.url().then(url => {
                        cy.log(url);
                        if (url.includes('/captcha') && cy.get('#srp-river-results > ul').length) {
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
                                                        //get the selling date
                                                        if ($listItem.find('.s-item__title--tagblock').length) {
                                                            cy.wait(waitTime);
                                                            cy.get('.s-item__title--tagblock').then((gameDate) => {
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

                                                        if (gameModel.adTitle && !gameArray.includes(gameModel)) {
                                                            gameArray.push(gameModel);
                                                        }
                                                        if (gameArray.length > 0) {
                                                            cy.insertMany(gameArray, 'games', 'testdb').then(res => {
                                                                cy.log(res); // print the id of inserted document
                                                            });
                                                        }
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
        }
    });
};

export default search;