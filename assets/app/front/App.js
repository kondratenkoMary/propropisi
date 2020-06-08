import * as Backbone from 'backbone';
import * as _ from 'underscore';

import Settings from './Settings';
import Utils from 'front/utils/Utils';
import Router from './Router';

import TopNav from 'front/components/Сommon/TopNav/TopNav';

import axios from 'axios';
import Cookies from 'js-cookie';

import 'front/reset.css';
import 'front/fonts.less';
import 'front/utils.less';
import 'front/style.less';
import {BACKBONE_EVENTS, CSS_PROPERTIES, SELECTORS, VIEWPORT_EVENTS} from './constants/Constants';

axios.interceptors.request.use(
    config => {
        config.headers['X-CSRFToken'] = Cookies.get('csrftoken') || $('meta[name="csrf-token"]')
            .attr('content');

        return config;
    },
    error => Promise.reject(error)
);

app.configure = Settings.configure;
app.configure();

app.vent = _.extend({}, Backbone.Events);

app.state = {};
app.utils = Utils;

app.els = {
    $window: $(window),
    $body: $(SELECTORS.body),
    $html: $(SELECTORS.html),
    $htmlBody: $(SELECTORS.htmlBody),
    $content: $(SELECTORS.content),
    $contentBody: $(SELECTORS.contentBody),
    $topNav: $(SELECTORS.topNav)
};

app.views = {
    topNav: new TopNav()
};

app.router = new Router();

app.router.start();

app.els.$window
    .on(VIEWPORT_EVENTS.load, () => {
        app.els.$content.css(CSS_PROPERTIES.visibility, '');

        window.app.vent.trigger(BACKBONE_EVENTS.windowLoaded);
    });
