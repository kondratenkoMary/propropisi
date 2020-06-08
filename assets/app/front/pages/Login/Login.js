import Base from 'front/components/Base/Base';

import * as _ from 'underscore';

import {VIEWPORT_EVENTS} from 'front/constants/Constants';

import './Login.less';

const Selectors = {
    btn: '.Login-rightSideCenterButton button'
};

const BindFunctions = [
    'onLogin'
];

export default class Login extends Base {
    events() {
        return {
            [`${VIEWPORT_EVENTS.click} ${Selectors.btn}`]: this.onLogin
        };
    }

    constructor(options = {}) {
        options.el = '.Login';
        super(options);

        $(window).on('load', () => {
            $('.Content').css('visibility', 'visible');
        });

        _.bindAll(this, BindFunctions);
    }

    onLogin() {

    }
}
