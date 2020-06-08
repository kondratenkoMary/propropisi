import Base from 'front/components/Base/Base';

import * as _ from 'underscore';

import './TaskStudent.less';

const Selectors = {
    el: '.TaskStudent'
};

const BindFunctions = [
    'onOpenTask'
];

export default class TaskStudent extends Base {
    constructor(options = {}) {
        options.el = Selectors.el;
        super(options);
        _.bindAll(this, BindFunctions);

        $(Selectors.el).on('click', this.onOpenTask);
    }

    onOpenTask(e) {
        const $item = $(e.currentTarget);
        const id = $item.data('id');

        app.vent.trigger('SolutionPopupStudent--open', id);
    }
};
