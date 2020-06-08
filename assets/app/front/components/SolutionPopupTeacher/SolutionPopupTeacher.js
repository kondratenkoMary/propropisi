import Base from 'front/components/Base/Base';

import * as _ from 'underscore';

import './SolutionPopupTeacher.less';

import {VIEWPORT_EVENTS, CSS_CLASSES} from 'front/constants/Constants';

const Selectors = {
    el: '.SolutionPopupTeacher',
    close: '.SolutionPopupTeacher-infoClose',
    bg: '.SolutionPopupTeacher-bg',

    wrapperPopups: '.Teacher-popupsTask',
    prevBtn: '.SolutionPopupTeacher-navPrev',
    nextBtn: '.SolutionPopupTeacher-navNext',

    agreeBtn: '.SolutionPopupTeacher-markAgree'
};

const BindFunctions = [
    'onOpenSolution',
    'onCloseSolution',
    'onPrevSolution',
    'onNextSolution'
];

export default class SolutionPopupTeacher extends Base {
    events() {
        return {
            [`${VIEWPORT_EVENTS.click} ${Selectors.close}`]: this.onCloseSolution,
            [`${VIEWPORT_EVENTS.click} ${Selectors.bg}`]: this.onCloseSolution,
            [`${VIEWPORT_EVENTS.click} ${Selectors.prevBtn}`]: this.onPrevSolution,
            [`${VIEWPORT_EVENTS.click} ${Selectors.nextBtn}`]: this.onNextSolution,
            [`${VIEWPORT_EVENTS.click} ${Selectors.agreeBtn}`]: this.onNextSolution
        };
    }

    constructor(options = {}) {
        options.el = '.SolutionPopupTeacher';
        super(options);

        _.bindAll(this, BindFunctions);

        app.vent.on('SolutionPopupTeacher--open', this.onOpenSolution);
    }

    onOpenSolution(id) {
        this.idOpenTask = id;

        $(Selectors.wrapperPopups + '[data-id="' + id + '"]')
            .find(Selectors.el)
            .first()
            .addClass(CSS_CLASSES.active);
    }

    onCloseSolution() {
        $(Selectors.el + '[data-id="' + this.idOpenTask + '"]').removeClass(CSS_CLASSES.active);
    }

    onPrevSolution() {
        const $curItem = $(Selectors.wrapperPopups + '[data-id="' + this.idOpenTask + '"]')
            .find(Selectors.el + '.' + CSS_CLASSES.active);

        const prevElement = $curItem.prev();

        $curItem.removeClass(CSS_CLASSES.active);

        if (!!prevElement.length) {
            prevElement.addClass(CSS_CLASSES.active);
        } else {
            this.onCloseSolution();
        }
    }

    onNextSolution() {
        const $curItem = $(Selectors.wrapperPopups + '[data-id="' + this.idOpenTask + '"]')
            .find(Selectors.el + '.' + CSS_CLASSES.active);

        const nextElement = $curItem.next();
        console.log(nextElement);

        $curItem.removeClass(CSS_CLASSES.active);

        if (!!nextElement.length) {
            nextElement.addClass(CSS_CLASSES.active);
        } else {
            this.onCloseSolution();
        }
    }
};
