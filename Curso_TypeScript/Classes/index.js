"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.User = void 0;
var User = /** @class */ (function () {
    function User(id, name, isAdmin) {
        this.id = id;
        this.name = name;
        this.isAdmin = isAdmin;
    }
    User.prototype.salute = function () {
        return "Hello, my name is ".concat(this.name);
    };
    User.prototype.getId = function () {
        return this.id;
    };
    User.prototype.getIsAdmin = function () {
        return this.isAdmin;
    };
    return User;
}());
exports.User = User;
