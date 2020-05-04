var prevMsg = "";

function start_websocket() {
    $(document).ready(function() {
	if (!window.console) window.console = {};
	if (!window.console.log) window.console.log = function() {};

	$("#messageform").on("submit", function() {
            newMessage($(this));
            return false;
    });
    $(document).ready(function(){

        $("#submitBtn").click(function(){        
    
            $("#messageform").submit();
    
    });
});
	$("#messageform").on("keypress", function(e) {
            if (e.keyCode == 13) {
		newMessage($(this));
		return false;
            } 
    });


    
	$("#command").select();
	updater.start();
    });
}

function newMessage(form) {
    msg = document.getElementById('inputbox').value;
    if(msg!="undefined")
        prevMsg = msg;
    var message = form.formToDict();
    updater.socket.send(JSON.stringify(message));
    form.find("input[type=text]").val("").select();
}

jQuery.fn.formToDict = function() {
    var fields = this.serializeArray();
    var json = {}
    for (var i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value;
    }
    if (json.next) delete json.next;
    return json;
};

function saveMessage() {
    var message = {"type":"save"};
    updater.socket.send(JSON.stringify(message));
    form.find("input[type=text]").val("").select();
}

function resetMessage() {
    var message = {"type":"reset"};
    updater.socket.send(JSON.stringify(message));
    form.find("input[type=text]").val("").select();
}

function scroll_to_bottom() {
    $("#inbox").animate({scrollTop:$("#inboxcontents").height()}, 1000);
}

var updater = {
    socket: null,

    start: function() {
        var url = "ws://" + location.host + "/websocket";
	updater.socket = new WebSocket(url);
	updater.socket.onmessage = function(event) {
	    updater.showMessage(JSON.parse(event.data));
	}
    },

    showMessage: function(message) {
	var html = "<div class=\"alert mud-"+message.type+"\">"+message.html+"</div>"
        $("#inboxcontents").append(html);
	scroll_to_bottom();
    }
};

function btEat()
{
    if(!$("#btEat").prop("disabled"))
    {
        let rep1 = "<div class='alert mud-result'>Le chien fuie à travers une petite trappe que vous venez d'apercevoir à côté de la grande porte au nord.</div>";
        $("#inboxcontents").append(rep1);
        updateBt();
    }
};

function btTouch()
{
    if(!$("#btTouch").prop("disabled"))
    {
        rep1 = "<div class='alert mud-result'>Le chien tout fier vous indique d'<tt>aboyer</tt> pour ouvrir la grande porte au nord. Il court ensuite vers une trappe à côté de la grande porte au nord.</div>";
        rep2 = "<div class='alert mud-info'> Il vous fait comprendre qu'il vous serait préférable d'éviter frapper qui ce soit en ces lieux."
        $("#inboxcontents").append(rep1,rep2);
        updateBt();
    }
};

function updateBt(){
    $("#btEat").prop('disabled',true);
    $("#btTouch").prop('disabled',true);
    scroll_to_bottom();
}



function inputKeyDown(e)
{
    //  up arrow
    if(e.keyCode == 38)
    {
        document.getElementById('inputbox').value = prevMsg
    }
    
}


