import Base from 'front/components/Base/Base';

import TasksListTeacher from 'front/components/TasksListTeacher/TasksListTeacher';
import SolutionPopupTeacher from 'front/components/SolutionPopupTeacher/SolutionPopupTeacher';

import './Teacher.less';

export default class Teacher extends Base {
    constructor(options = {}) {
        options.el = '.Teacher';
        super(options);
    }

    viewsRegistration() {
        this.registerView('tasksListTeacher', new TasksListTeacher());
        this.registerView('solutionPopupTeacher', new SolutionPopupTeacher());
    }
}
