$(document).ready(function () {
    var ActionTemplate = function(name, actionType, target, time) {
        this.name = name;
        this.actionType = actionType;
        this.target = target;
        this.time = time != null ? time : new Date().toISOString();
    }

    var ActionTemplateListModel = function () {
        var self = this;
        self.itemToadd = ko.observable(null);
        self.cloudActions = ko.observableArray(['Cloud Server - Soft Reboot', 'Cloud Server - Hard Reboot'])
        self.actionTemplates = ko.observableArray([new ActionTemplate('Shutdown Cloud Server', 'shutdown', 'apache-dev1.testnode.org')]); 
     
        self.addItem = function (model, event) {
            this.actionTemplates.push(this.itemToadd());
        };
     
        self.removeSelected = function () {
            this.actionTemplates.removeAll(this.selectedItems());
            this.selectedItems([]); // Clear selection
        };
     
        self.sortItems = function() {
            this.actionTemplates.sort();
        };
    };
     
    ko.applyBindings(new ActionTemplateListModel());
});