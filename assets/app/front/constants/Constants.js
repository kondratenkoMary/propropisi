export const REGEXPS = {
    email: /.+@.+\..+/i,
    phone: /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im
};

export const SELECTORS = {
    topNav: '.TopNav',
    footer: '.Footer',
    uRoute: '.u-Route',
    body: 'body',
    contentBody: '.Content-body',
    content: '.Content',
    html: 'html',
    htmlBody: 'html,body'
};

export const VIEWPORT_EVENTS = {
    click: 'click',
    mouseEnter: 'mouseenter',
    mouseLeave: 'mouseleave',
    focus: 'focus',
    blur: 'blur',
    input: 'input',
    keyUp: 'keyup',
    change: 'change',
    mouseOver: 'mouseover',
    touchStart: 'touchstart',
    touchMove: 'touchmove',
    touchEnd: 'touchend',
    resize: 'resize',
    scroll: 'scroll',
    orientationChange: 'orientationchange',
    keyDown: 'keydown',
    submit: 'submit',
    popState: 'popstate',
    load: 'load'
};

export const BACKBONE_EVENTS = {
    windowLoaded: 'window-loaded'
};

export const CSS_CLASSES = {
    visible: 'isVisible',
    hidden: 'isHidden',
    active: 'isActive',
    open: 'isOpen',
    notFound: 'Page404'
};

export const CSS_PROPERTIES = {
    visibility: 'visibility'
};
