export default {
    name: 'raven',
    initialize: function(container, application) {
        Raven.config(
            'http://9b0ea040d8414b2180548e304cac5018@sentry.adamcoddington.net/2',
            {
                whitelistUrls: [
                    /inthe\.am/,
                    /127\.0\.0\.1/
                ]
            }
        ).install();
    }
};
