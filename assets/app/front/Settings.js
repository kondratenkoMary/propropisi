import Cookies from 'js-cookie';

import * as _ from 'underscore';
import * as Backbone from 'backbone';

export default class Settings {
    static csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    static configure() {
        $.ajaxSetup({
            beforeSend: (xhr, settings) => {
                let csrftoken;

                if (Settings.csrfSafeMethod(settings.type) && !this.crossDomain) {
                    csrftoken = Cookies.get('csrftoken');
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        });

        Backbone.Model.prototype.toJSON = () => {
            const json = _.clone(this.attributes);
            let attr;

            for (attr in json) {
                if (json.hasOwnProperty(attr)) {
                    if ((json[attr] instanceof Backbone.Model) || (json[attr] instanceof Backbone.Collection)) {
                        json[attr] = json[attr].toJSON();
                    }
                }
            }



            return json;
        };
    }
}
