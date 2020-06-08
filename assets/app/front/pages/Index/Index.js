import Base from 'front/components/Base/Base';

import TasksListStudent from 'front/components/TasksListStudent/TasksListStudent';
import SolutionPopupStudent from 'front/components/SolutionPopupStudent/SolutionPopupStudent';

import './Index.less';

export default class Index extends Base {
    constructor(options = {}) {
        options.el = '.Index';
        super(options);
    }

    viewsRegistration() {
        this.registerView('tasksListStudent', new TasksListStudent());
        this.registerView('solutionPopupStudent', new SolutionPopupStudent());
    }
}
