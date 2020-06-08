import {REGEXPS} from 'front/constants/Constants';

export default class Utils {
    static createEmptyPromise() {
        return new Promise(function (resolve) {
            resolve();
        });
    }

    static isValidEmail(email) {
        return REGEXPS.email.test(email);
    }

    static isValidPhone(phone) {
        return REGEXPS.phone.test(phone);
    }
}
