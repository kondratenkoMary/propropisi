import Base from 'front/components/Base/Base';

import * as _ from 'underscore';

import axios from 'axios';

import Urls from '../../../../js/django_js_reverse/reverse.js';

import './SolutionPopupStudent.less';

import {VIEWPORT_EVENTS, CSS_CLASSES} from 'front/constants/Constants';

const Selectors = {
    el: '.SolutionPopupStudent',
    close: '.SolutionPopupStudent-infoClose',
    bg: '.SolutionPopupStudent-bg',
    solution: '.SolutionPopupStudent-solution',
    send: '.SolutionPopupStudent-send',
    input: '.SolutionPopupStudent-solution input',
    preview: '.SolutionPopupStudent-solutionPreviewImg',
    fileName: '.SolutionPopupStudent-solutionPreviewName',
    delete: '.SolutionPopupStudent-solutionEditIcon--delete',
    sendBtn: '.SolutionPopupStudent-sendBtn'
};

const BindFunctions = [
    'onOpenSolution',
    'onCloseSolution',
    'onChangeSolution',
    'onDeleteSolution',
    'onSend'
];

export default class SolutionPopupStudent extends Base {
    events() {
        return {
            [`${VIEWPORT_EVENTS.click} ${Selectors.close}`]: this.onCloseSolution,
            [`${VIEWPORT_EVENTS.click} ${Selectors.bg}`]: this.onCloseSolution,
            [`${VIEWPORT_EVENTS.change} ${Selectors.input}`]: this.onChangeSolution,
            [`${VIEWPORT_EVENTS.click} ${Selectors.delete}`]: this.onDeleteSolution,
            [`${VIEWPORT_EVENTS.click} ${Selectors.sendBtn}`]: this.onSend
        };
    }

    constructor(options = {}) {
        options.el = '.SolutionPopupStudent';
        super(options);

        _.bindAll(this, BindFunctions);

        app.vent.on('SolutionPopupStudent--open', this.onOpenSolution);
    }

    onOpenSolution(id) {
        this.idOpenSolution = id;

        $(Selectors.el + '[data-id="' + id + '"]').addClass(CSS_CLASSES.active);
    }

    onCloseSolution() {
        $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]').removeClass(CSS_CLASSES.active);
    }

    onChangeSolution(e) {
        const images = e.target.files;

        for (let i = 0, f; f = images[i]; i++) {
            if (!f.type.match('image.*')) {
                continue;
            }

            this.reader = new FileReader();

            this.reader.onload = ((theFile) => {
                $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]')
                    .find(Selectors.solution)
                    .attr('data-status', -1);
                $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]')
                    .find(Selectors.send)
                    .attr('data-status', -1);

                return (e) => {
                    let div = document.createElement('div');
                    div.innerHTML = ['<img src="', e.target.result,
                        '" title="', escape(theFile.name), '"/>'].join('');

                    $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]')
                        .find(Selectors.preview)
                        .html(div);
                    $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]')
                        .find(Selectors.fileName)
                        .text(theFile.name);
                };
            })(f);

            this.reader.readAsDataURL(f);
        }
    }

    onDeleteSolution() {
        $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]').find(Selectors.input)[0].value = '';
        $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]').find(Selectors.solution)
            .attr('data-status', 0);
        $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]').find(Selectors.send)
            .attr('data-status', 0);

        $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]').find(Selectors.preview)
            .empty();
        $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]').find(Selectors.fileName)
            .empty();
    }

    onSend() {
        let data = new FormData;
        const imagefile = $(Selectors.el + '[data-id="' + this.idOpenSolution + '"]').find(Selectors.input)[0];

        data.append('img', imagefile.files[0]);

        let config = {
            headers: {'Content-Type': 'multipart/form-data'}
        };

        axios
            .put(Urls['front:api:solution-detail'](this.idOpenSolution), data, config)
            .then((response) => {
                console.log(response.data);
                window.location.reload();
            })
            .catch((error) => {
                console.log(error);
                alert('Can\'t upload file');
            });
    }
};
