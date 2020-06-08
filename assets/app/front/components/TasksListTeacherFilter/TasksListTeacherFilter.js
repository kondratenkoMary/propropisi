import Base from 'front/components/Base/Base';

import './TasksListTeacherFilter.less';

import * as _ from 'underscore';

import {VIEWPORT_EVENTS, CSS_CLASSES} from 'front/constants/Constants';

const Selectors = {
    el: '.TasksListTeacherFilter',
    filterText: '.TasksListTeacherFilter-selectText',
    filterMenu: '.TasksListTeacherFilter-selectMenu',
    filterMenuItem: '.TasksListTeacherFilter-selectMenuItem',
    filterMenuCheckbox: '.TasksListTeacherFilter-selectMenuItem input'
};

const BindFunctions = [
    'onClickFilter',
    'onCloseFilter',
    'onChangeFilter',
    'setTexts',
    'onApplyFilters'
];

export default class TasksListTeacherFilter extends Base {
    events() {
        return {
            [`${VIEWPORT_EVENTS.click} ${Selectors.filterText}`]: this.onClickFilter,
            [`${VIEWPORT_EVENTS.change} ${Selectors.filterMenuCheckbox}`]: this.onChangeFilter
        };
    }

    constructor(options = {}) {
        options.el = Selectors.el;
        super(options);

        _.bindAll(this, BindFunctions);
        this.isOpenFilter = false;

        $(document).mouseup((e) => {
            const $popup = this.$(Selectors.filterMenu);
            const $select = this.$(Selectors.filterText);

            if (e.target !== $popup[0]
                && !$popup.has(e.target).length
                && e.target !== $select[0]
                && !$select.has(e.target).length) {
                this.onCloseFilter();
            }
        });
    }

    onClickFilter(e) {
        if (e.currentTarget !== this.$(Selectors.filterMenu)[0] && !this.$(Selectors.filterMenu).has(e.target).length) {
            this.isOpenFilter = !this.isOpenFilter;
            this.$(Selectors.filterMenu).toggleClass(CSS_CLASSES.open, this.isOpenFilter);
        }
    }

    onCloseFilter() {
        this.isOpenFilter = false;
        this.$(Selectors.filterMenu).removeClass(CSS_CLASSES.open);
    }

    onChangeFilter() {
        const $items = this.$(Selectors.filterMenuItem);
        const data = [];

        _.each($items, (item) => {
            const $item = $(item);

            if ($item.find('input')[0].checked) {
                data.push({
                    id: $item.data('id'),
                    text: $item.find('span').text()
                });
            }
        });

        this.setTexts(data);

        this.onApplyFilters(data);

        this.onCloseFilter();
    }

    setTexts(data) {
        this.$(Selectors.filterText).empty();

        if (data.length && data.length < 2) {
            _.each(data, (item) => {
                this.$(Selectors.filterText)
                    .append(
                        '<span class="TasksListTeacherFilter-selectText--' + item.id + '">' + item.text + '</span>'
                    );
            });
        } else {
            this.$(Selectors.filterText)
                .append('<span>' + this.$(Selectors.filterText).data('default') + '</span>');
        }
    }

    onApplyFilters(data) {
        app.vent.trigger('TasksListTeacher-filter', data);
    }
};
