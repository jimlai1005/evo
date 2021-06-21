
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
	$('.ua-success-message').show();
	$('.ua-error-message').show();

	$('#ua').show();
	$('#dgl').hide();
	$('#gh').hide();
	$('#gs').hide();
	$('#ow').hide();
	$('#iframetag').hide();
	$('#csid').hide();
	$('#ecomp').hide();

	$('#uaBtn').click(function() {
	  $('#ua').show();
	  $('#dgl').hide();
	  $('#gh').hide();
	  $('#gs').hide();
	  $('#ow').hide();
	  $('#iframetag').hide();
	  $('#csid').hide();
	  $('#ecomp').hide();

	});
	$('#dglBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').show();
	  $('#gh').hide();
	  $('#gs').hide();
	  $('#ow').hide();
	  $('#iframetag').hide();
	  $('#csid').hide();
	  $('#ecomp').hide();

	});
	$('#ghBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').hide();
	  $('#gh').show();
	  $('#gs').hide();
	  $('#ow').hide();
	  $('#iframetag').hide();
	  $('#csid').hide();
	  $('#ecomp').hide();

	});
	$('#gsBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').hide();
	  $('#gh').hide();
	  $('#gs').show();
	  $('#ow').hide();
	  $('#iframetag').hide();
	  $('#csid').hide();
	  $('#ecomp').hide();

	});
	$('#owBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').hide();
	  $('#gh').hide();
	  $('#gs').hide();
	  $('#ow').show();
	  $('#iframetag').hide();
	  $('#csid').hide();
	  $('#ecomp').hide();

	});
	$('#iframetagBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').hide();
	  $('#gh').hide();
	  $('#gs').hide();
	  $('#ow').hide();
	  $('#iframetag').show();
	  $('#csid').hide();
	  $('#ecomp').hide();

	});
	$('#csidBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').hide();
	  $('#gh').hide();
	  $('#gs').hide();
	  $('#ow').hide();
	  $('#iframetag').hide();
	  $('#csid').show();
	  $('#ecomp').hide();

	});

	$('#ecompBtn').click(function() {
	  $('#ua').hide();
	  $('#dgl').hide();
	  $('#gh').hide();
	  $('#gs').hide();
	  $('#ow').hide();
	  $('#iframetag').hide();
	  $('#csid').hide();
	  $('#ecomp').show();

	});
	
	$('#liveBtn').click(function() {
	  $('.ua-category').val('blackjack');
	  $('.ua-tid').val('g48qnr279zcxecmd');
	});

	$('#lobbyBtn').click(function() {
	  $('.ua-category').val('blackjack');
	  $('.ua-tid').val('');
	});

	$('#rtBtn').click(function() {
	  $('.ua-category').val('10001nights');
	  $('.ua-tid').val('10001nights00000');
	});

	$('#neBtn').click(function() {
	  $('.ua-category').val('bloodsuckers');
	  $('.ua-tid').val('bloodsuckers0000');
	});

	$('.ua form').submit(function(e) {
		$('.ua-success-message').html('');
		$('.ua-error-message').html('');

		var uaGame = {};
		if ($('.ua-tid').val().trim() == '') {
			uaGame = {
		        // "category": 'rng',
		        "category": $('.ua-category').val().trim(),
		        "interface": $('.ua-interface').val().trim(),
		        "playMode": $('.ua-playMode').val().trim() 
		    };
		}
		else {
			uaGame = {
		        // "category": 'rng',
		        "category": $('.ua-category').val().trim(),
		        "interface": $('.ua-interface').val().trim(),  
		        "table": {
		          "id": $('.ua-tid').val().trim()
		        },
		        "playMode": $('.ua-playMode').val().trim() 
		    };
		}

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
		      "game": uaGame,
		      "channel": {
		        "wrapped": ($('.ua-wrapped').val().trim() == 'true'),
		        "mobile": ($('.ua-mobile').val().trim() == 'true')
		      },
		      "urls": {
		        "cashier": $('.ua-cashier').val().trim(),
		        "responsibleGaming": $('.ua-responsibleGaming').val().trim(),
		        "lobby": $('.ua-lobby').val().trim(),
		        "sessionTimeout": $('.ua-sessionTimeout').val().trim(),
		        "gameHistory": "http://www.RGam.ee",
				"realityCheckURL": "http://www.RGam.ee",
				"rngGoLiveURL": "http://www.RGam.ee",
				"rngGoLiveURLMobile": "http://www.RGam.ee",
				"rngLobbyButton": "http://www.RGam.ee",
				"rngCloseButton": "http://www.RGam.ee",
				"rngHomeButton": "http://www.RGam.ee",
				"rngSessionTimeout": "http://www.RGam.ee",
				"rngErrorHandling": "http://www.RGam.ee",
				"sweSelfTest": "http://www.RGam.ee",
				"sweGameLimits": "http://www.RGam.ee",
				"sweSelfExclusion": "http://www.RGam.ee"
				},
		      "freeGames": ($('.ua-freeGames').val().trim() == 'true')
		}
	};
		e.preventDefault();
	    var postdata = $('.ua form').serialize();
	    formDataString = JSON.stringify(formData);
	    $.ajax({
	        type: 'POST',
	        contentType: 'application/json',
	        url: 'https://' + $('.ua-hostname').val().trim() + '/ua/v1/' + $('.ua-casino').val().trim() + '/' + $('.ua-api').val().trim() + '',
	        data: formDataString,
	        dataType: 'json',
	        success: function(json) {
	        	if (json){
		        	// $('.ua-success-message').html(json.entry);
		        	$('.ua-success-message').html('<a target="_blank" href="https://' + $('.ua-hostname').val().trim() + json.entry +'">Casino Entry Link</a>');
		        	$('.ua-success-message').fadeIn();
		        	// $('.ua-error-message').html(json.entryEmbedded);
		        	$('.ua-error-message').html('<a target="_blank" href="https://' + $('.ua-hostname').val().trim() + json.entryEmbedded +'">Casino Entry Embedded Link</a>');
		        	$('.ua-error-message').fadeIn();
		        }
		        else{
		        	jsonErrors = jQuery.parseJSON(json.errors);
		        	$('.ua-success-message').html(jsonErrors.code);
		        	$('.ua-success-message').fadeIn();
		        	$('.ua-error-message').html(jsonErrors.message);
		        	$('.ua-error-message').fadeIn();
		        }
	        }
	    });
	});

// DGL State API

	$('.dgl form').submit(function(e) {
		e.preventDefault();
	    var postdata = $('.dgl form').serialize();
	    // formDataString = JSON.stringify(formData);
	    
	    $.ajax({
	        type: 'GET',
	        contentType: 'application/json',
	        url: 'https://' + $('.dgl-casino_id').val().trim() + ":" + $('.dgl-api').val().trim() + "@" + $('.dgl-licensee_hostname').val().trim() + '/api/lobby/v1/' + $('.dgl-casino_id').val().trim() + '/state',
	        data: '',
	        dataType: 'json',
	        success: function(json) {
	        	if (json){
		        	// $('.dgl-success-message').html(json.entry);
		        	$('.dgl-success-message').html('players: ' + json.players + ' <br>ID: ' + json.id + ' <br>Casino ID : ' + json.casinoId + ' <br><br>tables: ' + JSON.stringify(json.tables));
		        	$('.dgl-success-message').fadeIn();
		        	// $('.dgl-error-message').html(json.entryEmbedded);
		        	// $('.dgl-error-message').html(JSON.stringify(tableName));
		        	// $('.dgl-error-message').html('tables: ' + JSON.stringify(json.tables));
		        	// $('.dgl-error-message').fadeIn();
		        }
		        else{
		        	jsonErrors = jQuery.parseJSON(json.errors);
		        	$('.dgl-success-message').html(jsonErrors.code);
		        	$('.dgl-success-message').fadeIn();
		        	$('.dgl-error-message').html(jsonErrors.message);
		        	$('.dgl-error-message').fadeIn();
		        }
	        },
	    });
	});

// GH API	
	$('.gh form').submit(function(e) {
		e.preventDefault();
	    var postdata = $('.gh form').serialize();
	    // formDataString = JSON.stringify(formData);
	    auth = $('.gh-casino_id').val().trim() + ":" + $('.gh-api').val().trim() ;
    	base64Encode = 'Basic ' + btoa(auth);

	    $.ajax({
	        type: 'GET',
	        contentType: 'application/json',
	        url: 'https://' + $('.gh-licensee_hostname').val().trim() + '/api/gamehistory/v1/casino/games',
	        headers: {'Authorization': base64Encode},
	        data: '',
	        dataType: 'json',
	        success: function(json) {
	        	if (json){
		        	// $('.gh-success-message').html(json.entry);
		        	$('.gh-success-message').html('UUID: ' + json.uuid + ' <br>Timestamp: ' + json.timestamp + ' <br><br>data: ' + JSON.stringify(json.data));
		        	$('.gh-success-message').fadeIn();
		        	// $('.gh-error-message').html(json.entryEmbedded);
		        	// $('.gh-error-message').html('tables: ' + JSON.stringify(json.tables));
		        	// $('.gh-error-message').fadeIn();
		        }
		        else{
		        	jsonErrors = jQuery.parseJSON(json.errors);
		        	$('.gh-success-message').html(jsonErrors.code);
		        	$('.gh-success-message').fadeIn();
		        	$('.gh-error-message').html(jsonErrors.message);
		        	$('.gh-error-message').fadeIn();
		        }
	        },
	    });
	});

// GS API	
	$('.gs form').submit(function(e) {
		e.preventDefault();
	    var postdata = $('.gs form').serialize();
	    // formDataString = JSON.stringify(formData);
	    auth = $('.gs-casino_id').val().trim() + ":" + $('.gs-api').val().trim() ;
    	base64Encode = 'Basic ' + btoa(auth);
    	timeNow = new Date(new Date().getTime() + new Date().getTimezoneOffset() * 60000 * 2).toISOString(); // - 24hrs
    	// $('.gs-iframeTag').html('<iframe frameBorder="0" width="1000" height="1345" scrolling="yes" src="https://' + $('.gs-licensee_hostname').val().trim() + '/api/streaming/game/v1/?startTime=' + timeNow +'"></iframe>');

    	var lastResponseLength = false;
	    $.ajax({
	        type: 'GET',
	        contentType: 'application/json',
	        // url: 'https://' + $('.gs-licensee_hostname').val().trim() + '/api/streaming/game/v1/?transmissionId=76332d312d302d35342d31363134303634373132313735',
	        url: 'https://' + $('.gs-licensee_hostname').val().trim() + '/api/streaming/game/v1/?startTime=' + timeNow,
	        headers: {'Authorization': base64Encode},
	        data: '',
	        dataType: 'json',
	        beforeSend: function(){
	        	//console.log('beforeSend')
	        	$('.gs-success-message').html('Please check the console log...');
			   	// $('.gs-success-message').html(JSON.stringify(json));
			    $('.gs-success-message').fadeIn();
	    	},
	    	xhrFields: {
	    		onprogress: function(e){
	    			//console.log('listening...')
	    			//console.log(e)
	    			var progressResponse;
               		var response = e.currentTarget.response;
               		if(lastResponseLength === false)
               		{
               		    progressResponse = response;
               		    lastResponseLength = response.length;
               		}
               		else
               		{
               		    progressResponse = response.substring(lastResponseLength);
               		    lastResponseLength = response.length;
               		    if (response.length != 0){
               		    	//var parsedResponse = JSON.parse(progressResponse);
               				console.log(progressResponse);
               		    }
               		}
	    		}
	    	},
		    success: function(json) {
		    	//console.log('success...')
		       	if (json){
		       		content = 'transmissionId: ' + json.transmissionId + ' <br>messageType: ' + json.messageType + ' <br><br>data: ' + JSON.stringify(json.data) + $('.gs-success-message').html();
			       	$('.gs-success-message').html(content);
			       	// $('.gs-success-message').html(JSON.stringify(json));
			       	$('.gs-success-message').fadeIn();
			       	$('.gs-error-message').html('');
			       	// $('.gs-error-message').html('tables: ' + JSON.stringify(json.tables));
			       	$('.gs-error-message').fadeIn();
			       	//console.log(content)
			       }
			       else{
			       	jsonErrors = jQuery.parseJSON(json.errors);
			       	$('.gs-success-message').html(jsonErrors.code);
			       	$('.gs-success-message').fadeIn();
			       	$('.gs-error-message').html(jsonErrors.message);
			       	$('.gs-error-message').fadeIn();
			       }
			   },
		    complete: function(json){
		    	if (json){
		    		//console.log(content)
		    	}
		    	//console.log('complete')
		    }
	    });
	});

// CSID API	
	$('.csid form').submit(function(e) {
		e.preventDefault();
	    var postdata = $('.csid form').serialize();
	    // formDataString = JSON.stringify(formData);
		casino_id = ($('.csid-casino_name').val().toLowerCase().replace(' ','') + "000000000000000").substr(0,15)+ "1";
		casino_name = $('.csid-casino_name').val().toLowerCase().replace(' ','');
		$('.csid-success-message').html(casino_name);
		// $('.csid-success-message').html(JSON.stringify(json));
		$('.csid-success-message').fadeIn();
		$('.csid-error-message').html(casino_id);
		// $('.csid-error-message').html('tables: ' + JSON.stringify(json.tables));
		$('.csid-error-message').fadeIn();
    	// $('.csid-iframeTag').html('<iframe frameBorder="0" width="1000" height="1345" scrolling="yes" src="https://' + $('.csid-licensee_hostname').val().trim() + '/api/streaming/game/v1/?startTime=' + timeNow +'"></iframe>');
	});

// ECOMP API	
	$('.ecomp form').submit(function(e) {
		e.preventDefault();
	    var postdata = $('.ecomp form').serialize();
	    // formDataString = JSON.stringify(formData);
		casino_id = ($('.ecomp-casino_name').val().toLowerCase().replace(' ','') + "000000000000000").substr(0,15)+ "1";
		casino_name = $('.ecomp-casino_name').val().toLowerCase().replace(' ','');
		context = '<div style="text-align:left">\
			<br>Dear Licensee,\
			<br>\
			<br>Hope to find you well. \
			<br>\
			<br>The information below is going to help you to build up your services, pass the tests and launch your games. Now, please allow me to explain the process as below:\
			<br>\
			<br>- Process:\
			<br>\
			<br>1. API Test: There is no user interface required in this phase. Only http request and response are needed. The purpose is to verify the wallet service works as expected. You will need the Staging Credentials, Online Documents and Table List as below to do it and please whitelist the following IPs: 87.246.163.0/24, 35.157.123.250, and 72.2.49.45.\
			<br>\
			<br>2. QA Test: In this phase, we focus on the user experience in the testing website. The test starts on players to login your testing website, launch Evolution games, place bets and etc. \
			<br>\
			<br>3. Config Production: Once above tests are passed, we will setup the production config for you. Then, after a quick check in production, you will be ready to go!\
			<br>\
			<br>- Staging Credentials:\
			<br>\
			<br>    Casino id: ' + casino_id + '\
			<br>\
			<br>    {\
			<br>\
			<br>    "host" : "' + casino_name + '.uat1.evo-test.com",\
			<br>\
			<br>    "ua2Token" : "test123",\
			<br>\
			<br>    "gameHistoryApiToken" : "test123",\
			<br>\
			<br>    "externalLobbyApiToken" : "test123",\
			<br>\
			<br>    "ua2AuthenticationUrl" : "https://' + casino_name + '.uat1.evo-test.com/ua/v1/' + casino_id + '/test123",\
			<br>\
			<br>    "owAuthToken" : "8kZoqVAreAR0ZajzG"\
			<br>\
			<br>    }\
			<br>\
			<br>- Online Documents:\
			<br>\
			<br>    1. User Authentication API (to launch games)\
			<br>\
			<br>    https://' + casino_name + '.uat1.evo-test.com/api/userauthentication/docs/v2/protocol.html\
			<br>\
			<br>    2. Game Streaming API (for instant game round records)\
			<br>\
			<br>    https://' + casino_name + '.uat1.evo-test.com/api/streaming/game/docs/index.html\
			<br>\
			<br>    3. Game History API\
			<br>\
			<br>    https://' + casino_name + '.uat1.evo-test.com/api/gamehistory/docs/index.html\
			<br>\
			<br>    4. Direct Game Launch API (for getting status of current lobby)\
			<br>\
			<br>    https://' + casino_name + '.uat1.evo-test.com/api/lobby/docs/index.html\
			<br>\
			<br>    5. One wallet API\
			<br>\
			<br>    https://' + casino_name + '.uat1.evo-test.com/api/evo-std-rest/docs/index.html\
			<br>\
			<br>- Table List:\
			<br>\
			<br>    Please find the table list information for your reference in the attachment and also note the tables in production may differ from staging as it depends on your contract with our commercial team.\
			<br>\
			<br>Anything, please feel free to let me know. Thank you.\
			<br>\
			</div>'
		$('.ecomp-success-message').html($('.ecomp-casino_name').val().toLowerCase().replace(' ',''));
		$('.ecomp-success-message').html(context);
		$('.ecomp-success-message').fadeIn();
		$('.ecomp-error-message').html();
		// $('.csid-error-message').html('tables: ' + JSON.stringify(json.tables));
		$('.ecomp-error-message').fadeIn();
    	// $('.csid-iframeTag').html('<iframe frameBorder="0" width="1000" height="1345" scrolling="yes" src="https://' + $('.csid-licensee_hostname').val().trim() + '/api/streaming/game/v1/?startTime=' + timeNow +'"></iframe>');
	});

// iFrame API	
	$('.iframetag form').submit(function(e) {
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
			        "category": "Roulette",
			        "interface": $('.ua-interface').val().trim(),  
			        "table": {
			          "id": "o3gekheqzwoacalh"
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
	    var postdata = $('.iframetag form').serialize();
	    formDataString = JSON.stringify(formData);
	    $.ajax({
	        type: 'POST',
	        contentType: 'application/json',
	        url: 'https://' + $('.ua-hostname').val().trim() + '/ua/v1/' + $('.ua-casino').val().trim() + '/' + $('.ua-api').val().trim() + '',
	        data: formDataString,
	        dataType: 'json',
	        success: function(json) {
	        	if (json){
		        	// $('.ua-success-message').html(json.entry);
		        	$('.iframetag-success-message').html('<a target="_blank" href="https://' + $('.ua-hostname').val().trim() + json.entry +'">Casino Entry Link</a>');
		        	$('.iframetag-success-message').fadeIn();
		        	// $('.ua-error-message').html(json.entryEmbedded);
		        	$('.iframetag-error-message').html('<a target="_blank" href="https://' + $('.ua-hostname').val().trim() + json.entryEmbedded +'">Casino Entry Embedded Link</a>');
		        	$('.iframetag-error-message').fadeIn();
		        	// $('.iframeTagLive').html('<script>EvolutionGaming.init({ url:"https://' + $('.ua-hostname').val().trim() + json.entry +'",topBar: 0,topBarLandscape: 0,topBarPortrait: 0, sideBarLandscape: 0});</script>');
		        	$('.iframeTagLive').html('<iframe frameBorder="0" width="300" height="345" scrolling="no" src="https://' + $('.ua-hostname').val().trim() + json.entry +'"></iframe>');
		        }
		        else{
		        	jsonErrors = jQuery.parseJSON(json.errors);
		        	$('.iframetag-success-message').html(jsonErrors.code);
		        	$('.iframetag-success-message').fadeIn();
		        	$('.iframetag-error-message').html(jsonErrors.message);
		        	$('.iframetag-error-message').fadeIn();
		        }
	        }
	    });
	});



	
});

