module.exports = function (env) {
    let staticPath = '/static/';

    if (typeof window !== 'undefined') {
        staticPath = window.app.settings.staticUrl;
    }

    env.addGlobal('static', function (file) {
        return staticPath + file;
    }, true);

    env.addGlobal('url', function (name, params = {}) {
        params = params || {};

        return Urls[name].apply(null, params.args);
    }, true);
};
