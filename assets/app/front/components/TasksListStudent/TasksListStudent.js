import Base from 'front/components/Base/Base';

import * as _ from 'underscore';

import './TasksListStudent.less';

import TasksListStudentFilter from 'front/components/TasksListStudentFilter/TasksListStudentFilter';
import TaskStudent from 'front/components/TaskStudent/TaskStudent';

import {CSS_CLASSES} from 'front/constants/Constants';

const Selectors = {
    el: '.TasksListStudent',
    marks: '.TasksListStudent-footerMarks',
    marksItem: '.TasksListStudent-footerMarksItem',
    marksItemEnd: '.TasksListStudent-footerLineEnd',
    marksItemStart: '.TasksListStudent-footerLineStart',
    marksItemText: '.TasksListStudent-footerMarksItemText',

    item: '.TaskStudent'
};

const BindFunctions = [
    'setAvgRating',
    'onFiltered'
];

export default class TasksListStudent extends Base {
    constructor(options = {}) {
        options.el = Selectors.el;

        super(options);

        _.bindAll(this, BindFunctions);

        this.setAvgRating();

        this.$items = this.$(Selectors.item);

        app.vent.on('TasksListStudent-filter', this.onFiltered);
    }

    viewsRegistration() {
        this.registerView('tasksListStudentFilter', new TasksListStudentFilter());
        this.registerView('taskStudent', new TaskStudent());
    }

    setAvgRating() {
        const marks = [2, 3, 4, 5];
        const avgRating = Number(this.$(Selectors.marks).data('avg'));

        let curPathRating = avgRating - 2;
        curPathRating = Math.max(curPathRating, 0);
        const percentAvgRating = Math.round(curPathRating / 3 * 100);
        let curRating = 0;

        this.$(Selectors.marksItemEnd).attr('offset', percentAvgRating + '%');
        this.$(Selectors.marksItemStart).attr('offset', percentAvgRating + '%');

        _.each(marks, (item, id) => {
            if (Number(avgRating) >= item) {
                curRating = id;
            }
        });

        _.each(this.$(Selectors.marksItem), (item) => {
            const $item = $(item);
            const curMark = Number($item.data('id'));

            if (curMark <= curRating) {
                $item.addClass(CSS_CLASSES.active);
            }
        });

        this.$(Selectors.marksItem + '[data-id="' + curRating + '"] ' + Selectors.marksItemText)
            .addClass(CSS_CLASSES.active);
    }

    onFiltered(data) {
        const ids = _.map(data, (item) => item.id);

        _.each(this.$items, (item) => {
            const $item = $(item);
            const statusItem = $item.data('status');

            if (data.length === 4 || !data.length) {
                this.$items.removeClass(CSS_CLASSES.hidden);
            } else {
                $item.toggleClass(CSS_CLASSES.hidden, (ids.indexOf(statusItem) === -1));
            }
        });
    }
};
