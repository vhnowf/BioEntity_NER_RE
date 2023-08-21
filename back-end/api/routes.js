'use strict';
module.exports = function(app) {
  let articlesCtrl = require('./controllers/ArticlesController');

  app.route('/api/v1/articles')
    .get(articlesCtrl.get)
  app.route('/api/v1/article/:articleId')
    .get(articlesCtrl.detail);
  app.route('/api/v1/article/:articleId/relations')
    .get(articlesCtrl.relation);
  app.route('/api/v1/articles/search-term=:keyword')
    .get(articlesCtrl.search);
};
