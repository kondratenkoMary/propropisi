import Base from 'front/components/Base/Base';

import * as _ from 'underscore';

import {CSS_CLASSES} from 'front/constants/Constants';

import './TaskTeacher.less';

const Selectors = {
    el: '.TaskTeacher',
    statusItem: '.TaskTeacher-infoRatingStatusesItem',
    svg: '.TaskTeacher-infoRatingMarkCircle svg'
};

const BindFunctions = [
    'onOpenTask',
    'setGraphics'
];

export default class TaskTeacher extends Base {
    constructor(options = {}) {
        options.el = Selectors.el;
        super(options);
        _.bindAll(this, BindFunctions);

        this.setGraphics();

        $(Selectors.el).on('click', this.onOpenTask);

        $(window).on('resize', this.setGraphics);
    }

    onOpenTask(e) {
        const $item = $(e.currentTarget);
        const id = $item.data('id');

        app.vent.trigger('SolutionPopupTeacher--open', id);
    }

    setGraphics() {
        if (window.matchMedia('(max-width: 767px)').matches) return;

        _.each($(Selectors.el), (item) => {
            if (!$(item).hasClass(CSS_CLASSES.hidden)) {
                let offset = 0;

                _.each($(item).find(Selectors.svg), (svg) => {
                    const lengthCircle = $(svg).find('circle')[0]
                        .getTotalLength();

                    if (!$(svg).find('circle')
                        .hasClass('notFound')) {
                        const percent = $(svg).data('percent');
                        const curPercent = lengthCircle * percent / 100;
                        const offsetArray = lengthCircle - curPercent;

                        $(svg).css('stroke-dasharray', (curPercent + ' ' + offsetArray) + 'px');
                        $(svg).css('stroke-dashoffset', (curPercent + offset) + 'px');
                        offset += curPercent;
                    }
                });
            }
        });
    }
};
