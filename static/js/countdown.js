(function(window) {

	'use strict';

	function define_gbcountdown() {
		var GBCountdown = {};
		GBCountdown.end = new Date("03/08/2015 22:00:00");
		GBCountdown._second = 1000;
		GBCountdown._minute = GBCountdown._second * 60;
		GBCountdown._hour = GBCountdown._minute * 60;
		GBCountdown._day = GBCountdown._hour * 24;

		GBCountdown.startUpdating = function() {
			GBCountdown.timer = setInterval(GBCountdown.updateRemaining, 1000);
		}

		GBCountdown.stopUpdating = function() {
			clearInterval(GBCountdown.timer);
		}

		GBCountdown.updateRemaining = function() {
			console.log("updateRemaining");

			var now = new Date();

			console.log(now);

			var distance = GBCountdown.end - now;

			console.log(distance);

			if (distance < 0) {
				GBCountdown.stopUpdating();
				document.getElementById("gbCountdown").innerHTML = "DEADLINE PASSED!";
				return;
			}

			var days = Math.floor(distance / GBCountdown._day);
			var hours = Math.floor((distance % GBCountdown._day) / GBCountdown._hour);
			var minutes = Math.floor((distance % GBCountdown._hour) / GBCountdown._minute);
			var seconds = Math.floor((distance % GBCountdown._minute) / GBCountdown._second);

			document.getElementById("gbCountdown").innerHTML = "deadline: " + days + "days ";
			document.getElementById("gbCountdown").innerHTML += hours + "hrs ";
			document.getElementById("gbCountdown").innerHTML += minutes + "mins ";
			document.getElementById("gbCountdown").innerHTML += seconds + "secs";
		}

		return GBCountdown;
	}

	if (typeof(GBCountdown) === "undefined") {
		window.GBCountdown = define_gbcountdown();
	} else {
		console.log("GBCountdown already defined.");
	}

	GBCountdown.startUpdating();

})(window);