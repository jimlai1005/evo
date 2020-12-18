
jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
    $.backstretch("assets/img/backgrounds/1.jpg");
    
    /*
        Wow
    */
    new WOW().init();
    
    /*
	    Countdown initializer
	*/


	var now = new Date();
	//var countTo = 178 * 24 * 60 * 60 * 1000 + now.valueOf(); 
	var pre =  new Date(Date.now()).getTime();
	var post = new Date('2021/03/01 00:00:00').getTime();
	var countTo = post-pre+ now.valueOf();
   
	$('.timer').countdown(countTo, function(event) {
		$(this).find('.days').text(event.offset.totalDays);
		$(this).find('.hours').text(event.offset.hours);
		$(this).find('.minutes').text(event.offset.minutes);
		$(this).find('.seconds').text(event.offset.seconds);
	});
	
	/*
	    
	*/
	$('.ua-success-message').hide();
	$('.ua-error-message').hide();
	$('#ua').show();
	$('#dgl').hide();
	$('#gh').hide();
	$('#gs').hide();
	$('#ow').hide();

	$('#uaBtn').click(function() {
	  $('#ua').show();
	  $('#dgl').hide();
	  $('#gh').hide();
	  $('#gs').hide();
	  $('#ow').hide();
	});
	$('#dglBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').show();
	  $('#gh').hide();
	  $('#gs').hide();
	  $('#ow').hide();
	});
	$('#ghBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').hide();
	  $('#gh').show();
	  $('#gs').hide();
	  $('#ow').hide();
	});
	$('#gsBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').hide();
	  $('#gh').hide();
	  $('#gs').show();
	  $('#ow').hide();
	});
	$('#owBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').hide();
	  $('#gh').hide();
	  $('#gs').hide();
	  $('#ow').show();
	});
	
	$('.ua form').submit(function(e) {
		var formData = {
	        	"uuid": $('.ua-uuid').val().trim(),
			    "player": {
			      "id": $('.ua-pid').val().trim(),
			      "update": ($('.ua-update').val().trim() == 'true'),
			      "firstName": $('.ua-firstName').val().trim(),
			      "lastName": $('.ua-lastName').val().trim(),
			      "nickname": $('.ua-nickname').val().trim(),
			      "country": $('.ua-country').val().trim(),
			      "language": $('.ua-language').val().trim(),
			      "currency": $('.ua-currency').val().trim(),
			      "session": {
			        "id": $('.ua-sid').val().trim(),
			        "ip": $('.ua-sip').val().trim()
			      },
			      "group": {
			        "id": $('.ua-gid').val().trim(),
			        "action": $('.ua-action').val().trim()
			      }
			    },
			    "config": {
			      "brand": {
			        "id": $('.ua-bid').val().trim(),
			        "skin": $('.ua-skin').val().trim()
			      },
			      "game": {
			        "category": $('.ua-category').val().trim(),
			        "interface": $('.ua-interface').val().trim(),  
			        "table": {
			          "id": $('.ua-tid').val().trim()
			        }
			      },
			      "channel": {
			        "wrapped": ($('.ua-wrapped').val().trim() == 'true'),
			        "mobile": ($('.ua-mobile').val().trim() == 'true')
			      },
			      "urls": {
			        "cashier": $('.ua-cashier').val().trim(),
			        "responsibleGaming": $('.ua-responsibleGaming').val().trim(),
			        "lobby": $('.ua-lobby').val().trim(),
			        "sessionTimeout": $('.ua-sessionTimeout').val().trim()
			      },
			      "freeGames": ($('.ua-freeGames').val().trim() == 'true')
			    }
			};
		e.preventDefault();
	    var postdata = $('.ua form').serialize();
	    $.ajax({
	        type: 'POST',
	        contentType: 'application/json',
	        url: 'https://' + $('.ua-hostname').val().trim() + '/ua/v1/' + $('.ua-casino').val().trim() + '/' + $('.ua-api').val().trim() + '',
	        data: formDataString,
	        dataType: 'json',
	        success: function(json) {
	        	jsonBody = jQuery.parseJSON(json.body);
	        	if (!jsonBody.errors){
		        	$('.ua-success-message').html(jsonBody.entry);
		        	$('.ua-success-message').fadeIn();
		        	$('.ua-error-message').html(jsonBody.entryEmbedded);
		        	$('.ua-error-message').fadeIn();
		        }
		        else{
		        	$('.ua-success-message').html(jsonBody.errors.code);
		        	$('.ua-success-message').fadeIn();
		        	$('.ua-error-message').html(jsonBody.errors.message);
		        	$('.ua-error-message').fadeIn();
		        }
	        },

	    });
	});

	$('.dgl form').submit(function(e) {
		
		e.preventDefault();
	    var postdata = $('.dgl form').serialize();
	    $.ajax({
	        type: 'GET',
	        contentType: 'application/json',
	        url: 'https://' + $('.licensee_hostname').val().trim() + '/api/lobby/v1/' + $('.casino_id').val().trim() + '/state',
	        data: formDataString,
	        dataType: 'json',
	        success: function(json) {
	        	jsonBody = jQuery.parseJSON(json.body);
	        	if (!jsonBody.errors){
		        	$('.ua-success-message').html(jsonBody.entry);
		        	$('.ua-success-message').fadeIn();
		        	$('.ua-error-message').html(jsonBody.entryEmbedded);
		        	$('.ua-error-message').fadeIn();
		        }
		        else{
		        	$('.ua-success-message').html(jsonBody.errors.code);
		        	$('.ua-success-message').fadeIn();
		        	$('.ua-error-message').html(jsonBody.errors.message);
		        	$('.ua-error-message').fadeIn();
		        }
	        },

	    });
	});




});

