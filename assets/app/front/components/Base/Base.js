import * as Backbone from 'backbone';
import * as _ from 'underscore';
import Utils from 'front/utils/Utils';

export default class Base extends Backbone.View {
    constructor(options = {}) {
        super(options);
        this.options = options;

        this.views = {};
        this.template = options.template;
    }

    activate() {
        return new Promise((res) => {
            this.viewsRegistration();
            res();
        }).then(() => {
            let promise = Utils.createEmptyPromise();

            if (this.views) {
                promise = Promise.all(_.map(this.views, (view) => {
                    return view.activate();
                }));
            }

            return promise;
        });
    }

    deactivate(params = {}) {
        let promise = Utils.createEmptyPromise();

        if (this.views) {
            promise = Promise.all(_.map(this.views, (view) => {
                return view.deactivate(params);
            }));
        }


        return promise.then(() => {
            if (params.destroy) {
                this.destroy();
            }
        });
    }

    destroy() {
        this.undelegateEvents();
        this.$el.removeData().unbind();
        this.remove();
    }

    viewsRegistration() {
    }

    registerView(viewName, view) {
        this.views[viewName] = view;

        return view;
    }

    addView(view) {
        this.views.push(view);
    }

    getView(viewName) {
        return this.views[viewName];
    }

    destroyView(viewName) {
        this.views[viewName].destroy();
        delete this.views[viewName];
    }
}
