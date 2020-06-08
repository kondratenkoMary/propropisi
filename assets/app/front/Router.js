import * as Backbone from 'backbone';
import * as _ from 'underscore';
import {CSS_CLASSES} from 'front/constants/Constants';

export default class Router extends Backbone.Router {
    routes() {
        return {
            '': 'index',
            'teacher(/)': 'teacher',
            '404(/)': 'notFound'
        };
    };

    index() {
        this.importComponent('Index');
    }

    teacher() {
        this.importComponent('Teacher');
    }

    notFound() {
        this.importComponent('NotFound');
    }

    importComponent(pageName) {
        import('front/pages/' + pageName + '/' + pageName).then(({default: Component}) => {
            this.activate(Component);
        });
    }

    activate(view) {
        app.state.view = new view();
        app.state.view.activate();
    }

    start() {
        const is404 = app.els.$body.hasClass(CSS_CLASSES.notFound);
        const pushStateSupported = history && _.isFunction(history.pushState);
        Backbone.history.start({pushState: pushStateSupported, silent: is404, hashChange: false});


        if (is404) {
            this.notFound();
        }
    }
}
