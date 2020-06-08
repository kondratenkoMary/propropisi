import Base from 'front/components/Base/Base';

import * as _ from 'underscore';

import './TasksListTeacher.less';

import TasksListTeacherFilter from 'front/components/TasksListTeacherFilter/TasksListTeacherFilter';
import TaskTeacher from 'front/components/TaskTeacher/TaskTeacher';

import {CSS_CLASSES} from 'front/constants/Constants';

const Selectors = {
    el: '.TasksListTeacher',

    item: '.TaskTeacher'
};

const BindFunctions = [
    'onFiltered'
];

export default class TasksListTeacher extends Base {
    constructor(options = {}) {
        options.el = Selectors.el;

        super(options);

        _.bindAll(this, BindFunctions);
        this.$items = this.$(Selectors.item);

        app.vent.on('TasksListTeacher-filter', this.onFiltered);
    }

    viewsRegistration() {
        this.registerView('tasksListTeacherFilter', new TasksListTeacherFilter());
        this.registerView('taskTeacher', new TaskTeacher());
    }

    onFiltered(data) {
        const ids = _.map(data, (item) => item.id);

        _.each(this.$items, (item) => {
            const $item = $(item);
            const statusItem = $item.data('status');

            if (data.length === 2 || !data.length) {
                this.$items.removeClass(CSS_CLASSES.hidden);
            } else {
                $item.toggleClass(CSS_CLASSES.hidden, (ids.indexOf(statusItem) === -1));
            }
        });
    }
};
