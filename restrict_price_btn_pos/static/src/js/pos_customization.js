odoo.define('restrict_price_btn_pos.PriceButton', function (require) {
"use strict";

var models = require('point_of_sale.models');
    /** To load fields into model res user in pos **/
    models.load_fields('res.users', "price");

var screens = require('point_of_sale.screens');
var core = require('web.core');



});
